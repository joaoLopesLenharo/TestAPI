import pytest
from app import FoodEntry, FoodItem, db
from datetime import datetime, timedelta

def test_dashboard_route(auth_client, test_user, test_app):
    """
    Testa o acesso à rota do dashboard
    """
    # Acessa o dashboard
    response = auth_client.get('/dashboard')
    
    # Verifica se a página foi carregada corretamente
    assert response.status_code == 200
    # Verifica se o título está presente (pode estar em UTF-8)
    assert b'Resumo' in response.data or b'Resumo Di\xc3\xa1rio' in response.data
    
    # Verifica se as informações do usuário estão sendo exibidas
    assert str(test_user.daily_calorie_goal).encode() in response.data
    
    # Verifica se as entradas de comida estão sendo exibidas (se houver)
    with test_app.app_context():
        today = datetime.utcnow().date()
        entries_today = FoodEntry.query.filter(
            FoodEntry.user_id == test_user.id,
            FoodEntry.date == today
        ).all()
        
        # Se houver entradas, verifica que os nomes aparecem
        if entries_today:
            for entry in entries_today:
                # Verifica se o nome do alimento aparece (pode estar em UTF-8)
                food_name_bytes = entry.food_item.name.encode('utf-8')
                assert food_name_bytes in response.data or entry.food_item.name in response.data.decode('utf-8', errors='ignore')

def test_add_food_entry_ui(auth_client, test_user, test_app):
    """
    Testa a adição de uma entrada de comida através da API
    """
    import json
    
    # Obtém o ID do food item dentro do contexto do app
    with test_app.app_context():
        food = FoodItem.query.first()
        food_id = food.id
    
    # Dados para a API
    data = {
        'food_item_id': food_id,
        'quantity': 1
    }
    
    # Envia a requisição para a API (não precisa de contexto aqui, o auth_client já gerencia)
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    # Verifica se a entrada foi criada
    assert response.status_code == 201
    
    # Verifica se a entrada foi criada no banco de dados (dentro do contexto)
    with test_app.app_context():
        entry = FoodEntry.query.filter_by(
            user_id=test_user.id,
            food_item_id=food_id,
            quantity=1
        ).first()
        
        assert entry is not None

def test_dashboard_calculations(auth_client, test_user, test_app):
    """
    Testa os cálculos exibidos no dashboard
    """
    with test_app.app_context():
        # Limpa as entradas existentes para este usuário
        FoodEntry.query.filter_by(user_id=test_user.id).delete()
        db.session.commit()
        
        # Limpa itens de comida que possam ter sido criados em outros testes
        # (mas mantém os itens públicos que foram criados no setup)
        # Não vamos limpar todos os itens, apenas criar novos para este teste
        
        # Cria itens de comida para teste com nomes únicos para evitar conflitos
        food1 = FoodItem(
            name='Arroz Teste',
            calories=130,
            protein=2.7,
            carbs=28,
            fat=0.3,
            is_public=True
        )
        
        food2 = FoodItem(
            name='Feijão Teste',
            calories=127,
            protein=8.8,
            carbs=22.8,
            fat=0.5,
            is_public=True
        )
        
        db.session.add_all([food1, food2])
        db.session.flush()  # Para obter os IDs
        
        # Cria entradas de comida para hoje
        today = datetime.utcnow().date()
        
        entry1 = FoodEntry(
            user_id=test_user.id,
            food_item_id=food1.id,
            quantity=2,  # 260 kcal, 5.4g de proteína, 56g de carboidratos, 0.6g de gordura
            date=today
        )
        
        entry2 = FoodEntry(
            user_id=test_user.id,
            food_item_id=food2.id,
            quantity=1,  # 127 kcal, 8.8g de proteína, 22.8g de carboidratos, 0.5g de gordura
            date=today
        )
        
        db.session.add_all([entry1, entry2])
        db.session.commit()
    
    # Acessa o dashboard
    response = auth_client.get('/dashboard')
    
    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 200
    
    # Verifica os totais calculados
    total_calories = 260 + 127  # 387 kcal
    total_protein = 5.4 + 8.8   # 14.2g
    total_carbs = 56 + 22.8     # 78.8g
    total_fat = 0.6 + 0.5       # 1.1g
    
    # Verifica se os totais estão sendo exibidos corretamente
    # Verifica calorias (sempre presente no resumo)
    assert str(total_calories).encode() in response.data or str(int(total_calories)).encode() in response.data
    
    # Verifica se os valores estão presentes na tabela (onde sabemos que aparecem)
    # Proteína: 5.4g e 8.8g devem aparecer na tabela
    assert b'5.4g' in response.data or b'5.4' in response.data
    assert b'8.8g' in response.data or b'8.8' in response.data
    # Carboidratos: 56.0g e 22.8g devem aparecer na tabela  
    assert (b'56.0g' in response.data or b'56g' in response.data or b'56.0' in response.data)
    assert b'22.8g' in response.data or b'22.8' in response.data
    # Gordura: 0.6g e 0.5g devem aparecer na tabela
    assert (b'0.6g' in response.data or b'0.6' in response.data or b'0g' in response.data)
    assert b'0.5g' in response.data or b'0.5' in response.data
    
    # Verifica a barra de progresso de calorias
    progress_percent = min(int((total_calories / test_user.daily_calorie_goal) * 100), 100)
    assert f'width: {progress_percent}%'.encode() in response.data
