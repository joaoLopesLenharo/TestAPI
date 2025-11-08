import os
import tempfile
import pytest
from werkzeug.security import generate_password_hash
from app import app, db, User, FoodItem, FoodEntry
from datetime import datetime, timedelta

@pytest.fixture(scope='module')
def test_app():
    # Cria um arquivo temporário único para cada módulo de teste
    # Isso garante que cada módulo tenha seu próprio banco isolado
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    os.close(db_fd)  # Fecha o file descriptor, mas mantém o arquivo
    
    # Configura o aplicativo para testes
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Cria o banco de dados e carrega os dados de teste
    with app.app_context():
        db.drop_all()  # Garante que o banco está limpo
        db.create_all()
        setup_test_data()
    
    yield app
    
    # Limpeza após todos os testes do módulo
    with app.app_context():
        db.session.remove()
        db.drop_all()
        # Fecha todas as conexões do banco
        db.engine.dispose()
    
    # Remove o arquivo temporário após fechar todas as conexões
    try:
        if os.path.exists(db_path):
            os.unlink(db_path)
    except OSError:
        pass  # Arquivo já foi removido ou está em uso

@pytest.fixture(scope='module')
def test_client(test_app):
    # Cria um cliente de teste
    with test_app.test_client() as testing_client:
        # Estabelece um contexto de aplicativo
        with test_app.app_context():
            yield testing_client
            
            # Limpeza após o teste
            db.session.remove()
            db.drop_all()

def setup_test_data():
    # Como o banco foi limpo e recriado antes de chamar esta função,
    # podemos criar os dados diretamente sem verificar se existem
    
    # Cria um usuário de teste
    user = User(
        username='testuser',
        email='test@example.com',
        daily_calorie_goal=2000
    )
    user.set_password('test123')
    db.session.add(user)
    db.session.flush()  # Para obter o ID do usuário
    
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
    db.session.flush()  # Para obter os IDs dos itens
    
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
        password_hash=generate_password_hash('password123'),
        daily_calorie_goal=2500
    )
    return user

@pytest.fixture(scope='module')
def test_user(test_app):
    with test_app.app_context():
        return User.query.filter_by(username='testuser').first()

@pytest.fixture(scope='function')
def auth_client(test_client, test_user, test_app):
    # Realiza login
    with test_app.app_context():
        with test_client.session_transaction() as session:
            session['_user_id'] = str(test_user.id)
            session['_fresh'] = True
    
    # Retorna o cliente autenticado
    yield test_client
    
    # Limpa a sessão após o teste
    with test_app.app_context():
        with test_client.session_transaction() as session:
            session.clear()
