import os
import tempfile
import pytest
from app import app, db, User, FoodItem, FoodEntry
from datetime import datetime, timedelta

@pytest.fixture(scope='module')
def test_client():
    # Configuração do aplicativo para testes
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Cria um cliente de teste
    with app.test_client() as testing_client:
        # Estabelece um contexto de aplicativo
        with app.app_context():
            # Cria o banco de dados e as tabelas
            db.create_all()
            
            # Configuração de dados de teste
            setup_test_data()
            
            yield testing_client  # Aqui ocorre o teste
            
            # Limpeza após o teste
            db.session.remove()
            db.drop_all()

def setup_test_data():
    # Cria um usuário de teste
    hashed_password = User.generate_password_hash('test123')
    user = User(
        username='testuser',
        email='test@example.com',
        password_hash=hashed_password,
        daily_calorie_goal=2000
    )
    db.session.add(user)
    
    # Cria itens de comida de teste
    food1 = FoodItem(
        name='Maçã',
        calories=52,
        protein=0.3,
        carbs=14,
        fat=0.2
    )
    
    food2 = FoodItem(
        name='Frango Grelhado',
        calories=165,
        protein=31,
        carbs=0,
        fat=3.6
    )
    
    db.session.add_all([food1, food2])
    db.session.commit()
    
    # Cria entradas de comida para o usuário
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)
    
    entry1 = FoodEntry(
        user_id=user.id,
        food_item_id=food1.id,
        quantity=2,
        date=today
    )
    
    entry2 = FoodEntry(
        user_id=user.id,
        food_item_id=food2.id,
        quantity=1,
        date=yesterday
    )
    
    db.session.add_all([entry1, entry2])
    db.session.commit()

@pytest.fixture(scope='module')
def new_user():
    user = User(
        username='newuser',
        email='newuser@example.com',
        password_hash=User.generate_password_hash('password123'),
        daily_calorie_goal=2500
    )
    return user

@pytest.fixture(scope='module')
def test_user():
    return User.query.filter_by(username='testuser').first()

@pytest.fixture(scope='module')
def auth_client(test_client, test_user):
    # Realiza login para obter o token
    response = test_client.post('/login', data=dict(
        username='testuser',
        password='test123'
    ), follow_redirects=True)
    
    return test_client
