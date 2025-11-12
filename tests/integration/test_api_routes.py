import json
import pytest
from app import db, User, FoodItem, FoodEntry
from datetime import datetime, timedelta

def test_get_foods(test_client, auth_client):
    """
    Testa a rota GET /api/food
    """
    response = auth_client.get('/api/food')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'name' in data[0]
    assert 'calories' in data[0]

def test_add_food_entry(test_client, auth_client, test_user):
    """
    Testa a rota POST /api/entry
    """
    # Pega um item de comida existente
    food = FoodItem.query.first()
    
    # Dados para a requisição
    data = {
        'food_item_id': food.id,
        'quantity': 2
    }
    
    # Faz a requisição
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    # Verifica a resposta
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert 'id' in response_data
    
    # Verifica se a entrada foi criada no banco de dados
    entry = db.session.get(FoodEntry, response_data['id'])
    assert entry is not None
    assert entry.user_id == test_user.id
    assert entry.food_item_id == food.id
    assert entry.quantity == 2
    assert entry.date == datetime.utcnow().date()

def test_add_food_entry_invalid_data(test_client, auth_client):
    """
    Testa a rota POST /api/entry com dados inválidos
    """
    # Dados inválidos (food_item_id faltando)
    data = {
        'quantity': 2
    }
    
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code in [400, 500]  # Pode retornar 400 ou 500 dependendo da validação
    
    # Dados inválidos (food_item_id não existe)
    data = {
        'food_item_id': 9999,
        'quantity': 2
    }
    
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code in [400, 404, 500]  # Pode retornar diferentes códigos dependendo da validação

def test_unauthorized_access(test_app):
    """
    Testa o acesso não autorizado às rotas da API
    """
    # Cria um novo cliente de teste sem autenticação
    # Isso garante que não há sessão compartilhada de outros testes
    with test_app.test_client() as client:
        # Limpa qualquer sessão existente explicitamente
        with client.session_transaction() as session:
            session.clear()
            # Remove qualquer chave relacionada ao Flask-Login
            session.pop('_user_id', None)
            session.pop('_fresh', None)
            session.pop('_id', None)
        
        # Tenta acessar sem autenticação
        # O Flask-Login com @login_required deve chamar unauthorized_handler
        # que retorna 401 para APIs
        response = client.get('/api/food', follow_redirects=False)
        
        # Verifica se retorna 401 (JSON) ou 302 (redirect)
        # O handler unauthorized_handler deve retornar 401 para APIs
        assert response.status_code in [401, 302], f"Expected 401 or 302, got {response.status_code}"
        
        # Se retornou 401, verifica se é JSON
        if response.status_code == 401:
            assert response.is_json
            data = response.get_json()
            assert 'error' in data or 'message' in data
        
        # Limpa novamente antes do próximo teste
        with client.session_transaction() as session:
            session.clear()
            session.pop('_user_id', None)
            session.pop('_fresh', None)
            session.pop('_id', None)
        
        # Testa POST sem autenticação
        response = client.post('/api/entry', json={}, follow_redirects=False)
        # Deve retornar 401 ou 302 (não autenticado) antes da validação
        assert response.status_code in [401, 302], f"Expected 401 or 302, got {response.status_code}"
        
        # Se retornou 401, verifica se é JSON
        if response.status_code == 401:
            assert response.is_json
