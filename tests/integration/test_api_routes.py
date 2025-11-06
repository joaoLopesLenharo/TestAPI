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
        'food_id': food.id,
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
    assert 'entry_id' in response_data
    
    # Verifica se a entrada foi criada no banco de dados
    entry = FoodEntry.query.get(response_data['entry_id'])
    assert entry is not None
    assert entry.user_id == test_user.id
    assert entry.food_item_id == food.id
    assert entry.quantity == 2
    assert entry.date == datetime.utcnow().date()

def test_add_food_entry_invalid_data(test_client, auth_client):
    """
    Testa a rota POST /api/entry com dados inválidos
    """
    # Dados inválidos (food_id faltando)
    data = {
        'quantity': 2
    }
    
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 400
    
    # Dados inválidos (food_id não existe)
    data = {
        'food_id': 9999,
        'quantity': 2
    }
    
    response = auth_client.post(
        '/api/entry',
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 404

def test_unauthorized_access(test_client):
    """
    Testa o acesso não autorizado às rotas da API
    """
    # Tenta acessar sem autenticação
    response = test_client.get('/api/food')
    assert response.status_code == 401
    
    response = test_client.post('/api/entry', json={})
    assert response.status_code == 401
