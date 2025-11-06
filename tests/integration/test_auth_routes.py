import pytest
from app import User, db

def test_register_route(test_client):
    """
    Testa o registro de um novo usuário
    """
    # Dados do novo usuário
    user_data = {
        'username': 'newtestuser',
        'email': 'newtest@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    }
    
    # Envia a requisição de registro
    response = test_client.post('/register', data=user_data, follow_redirects=True)
    
    # Verifica se o redirecionamento ocorreu corretamente
    assert response.status_code == 200
    assert b'Login' in response.data
    
    # Verifica se o usuário foi criado no banco de dados
    user = User.query.filter_by(username='newtestuser').first()
    assert user is not None
    assert user.email == 'newtest@example.com'
    assert user.check_password('testpass123') is True

def test_login_route(test_client, test_user):
    """
    Testa o login de um usuário
    """
    # Dados de login
    login_data = {
        'username': 'testuser',
        'password': 'test123',
        'remember': False
    }
    
    # Envia a requisição de login
    response = test_client.post('/login', data=login_data, follow_redirects=True)
    
    # Verifica se o redirecionamento ocorreu para o dashboard
    assert response.status_code == 200
    assert b'Daily Summary' in response.data

def test_invalid_login(test_client):
    """
    Testa tentativa de login com credenciais inválidas
    """
    # Dados de login inválidos
    login_data = {
        'username': 'nonexistent',
        'password': 'wrongpassword',
        'remember': False
    }
    
    # Envia a requisição de login
    response = test_client.post('/login', data=login_data, follow_redirects=True)
    
    # Verifica se a mensagem de erro é exibida
    assert b'Invalid username or password' in response.data

def test_logout_route(test_client, auth_client):
    """
    Testa o logout de um usuário autenticado
    """
    # Faz logout
    response = auth_client.get('/logout', follow_redirects=True)
    
    # Verifica se o redirecionamento ocorreu para a página de login
    assert response.status_code == 200
    assert b'Login' in response.data
    
    # Tenta acessar uma rota protegida
    response = auth_client.get('/dashboard', follow_redirects=True)
    # Deve redirecionar para a página de login
    assert b'Please log in to access this page' in response.data
