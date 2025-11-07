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
    entry = FoodEntry.query.get(response_data['id'])
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

def test_unauthorized_access(test_client):
    """
    Testa o acesso não autorizado às rotas da API
    """
    # Tenta acessar sem autenticação
    response = test_client.get('/api/food')
    assert response.status_code in [401, 302]  # Pode redirecionar para login (302) ou retornar 401
    
    response = test_client.post('/api/entry', json={})
    assert response.status_code in [401, 302]  # Pode redirecionar para login (302) ou retornar 401
