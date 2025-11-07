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
    
    # Verifica se as entradas de comida estão sendo exibidas
    with test_app.app_context():
        today = datetime.utcnow().date()
        entries_today = FoodEntry.query.filter(
            FoodEntry.user_id == test_user.id,
            FoodEntry.date == today
        ).all()
        
        for entry in entries_today:
            assert entry.food_item.name.encode() in response.data

def test_add_food_entry_ui(auth_client, test_user, test_app):
    """
    Testa a adição de uma entrada de comida através da API
    """
    import json
    with test_app.app_context():
        # Pega um item de comida existente
        food = FoodItem.query.first()
        
        # Dados para a API
        data = {
            'food_item_id': food.id,
            'quantity': 1
        }
        
        # Envia a requisição para a API
        response = auth_client.post(
            '/api/entry',
            data=json.dumps(data),
            content_type='application/json'
        )
        
        # Verifica se a entrada foi criada
        assert response.status_code == 201
        
        # Verifica se a entrada foi criada no banco de dados
        entry = FoodEntry.query.filter_by(
            user_id=test_user.id,
            food_item_id=food.id,
            quantity=1
        ).first()
        
        assert entry is not None

def test_dashboard_calculations(auth_client, test_user, test_app):
    """
    Testa os cálculos exibidos no dashboard
    """
    with test_app.app_context():
        # Limpa as entradas existentes
        FoodEntry.query.filter_by(user_id=test_user.id).delete()
        db.session.commit()
        
        # Cria itens de comida para teste
        food1 = FoodItem(
            name='Arroz',
            calories=130,
            protein=2.7,
            carbs=28,
            fat=0.3
        )
        
        food2 = FoodItem(
            name='Feijão',
            calories=127,
            protein=8.8,
            carbs=22.8,
            fat=0.5
        )
        
        db.session.add_all([food1, food2])
        db.session.commit()
        
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
    
    # Verifica os totais calculados
    total_calories = 260 + 127  # 387 kcal
    total_protein = 5.4 + 8.8   # 14.2g
    total_carbs = 56 + 22.8     # 78.8g
    total_fat = 0.6 + 0.5       # 1.1g
    
    # Verifica se os totais estão sendo exibidos corretamente
    assert str(total_calories).encode() in response.data
    assert str(round(total_protein, 1)).encode() in response.data
    assert str(round(total_carbs, 1)).encode() in response.data
    assert str(round(total_fat, 1)).encode() in response.data
    
    # Verifica a barra de progresso de calorias
    progress_percent = min(int((total_calories / test_user.daily_calorie_goal) * 100), 100)
    assert f'width: {progress_percent}%'.encode() in response.data
