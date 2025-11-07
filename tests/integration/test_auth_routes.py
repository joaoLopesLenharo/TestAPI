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
    # Verifica se está no dashboard (pode ter diferentes textos)
    assert b'Resumo' in response.data or b'Dashboard' in response.data or b'Calorias' in response.data

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
    
    # Envia a requisição de login (sem follow_redirects para ver a mensagem)
    response = test_client.post('/login', data=login_data, follow_redirects=False)
    
    # Verifica se a mensagem de erro é exibida ou se redireciona de volta para login
    assert response.status_code in [200, 302]
    if response.status_code == 200:
        # Se não redirecionou, deve ter a mensagem de erro
        assert b'Invalid' in response.data or b'invalid' in response.data or b'username' in response.data.lower() or b'password' in response.data.lower()
    else:
        # Se redirecionou, segue o redirect e verifica
        response = test_client.post('/login', data=login_data, follow_redirects=True)
        assert b'Invalid' in response.data or b'invalid' in response.data or b'Login' in response.data

def test_logout_route(test_client, auth_client):
    """
    Testa o logout de um usuário autenticado
    """
    # Faz logout
    response = auth_client.get('/logout', follow_redirects=True)
    
    # Verifica se o redirecionamento ocorreu para a página inicial ou login
    assert response.status_code == 200
    # Pode estar na página inicial ou login
    assert b'Login' in response.data or b'Entrar' in response.data or b'Track Your Calories' in response.data
    
    # Tenta acessar uma rota protegida (sem seguir redirects primeiro)
    response = auth_client.get('/dashboard', follow_redirects=False)
    # Deve redirecionar (302) ou mostrar mensagem de erro
    assert response.status_code in [302, 401, 403]
