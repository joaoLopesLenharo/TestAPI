import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    # Configura o navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Inicializa o navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos
    
    yield driver
    
    # Fecha o navegador após os testes
    driver.quit()

def test_user_registration_and_login(browser, test_client, test_user):
    """
    Testa o fluxo completo de registro e login de um novo usuário
    """
    # Acessa a página inicial
    browser.get('http://localhost:5000/')
    
    # Verifica se a página inicial foi carregada
    assert "Calorie Tracker" in browser.title
    
    # Clica no link de registro
    register_link = browser.find_element(By.LINK_TEXT, "Register")
    register_link.click()
    
    # Preenche o formulário de registro
    username = browser.find_element(By.NAME, "username")
    email = browser.find_element(By.NAME, "email")
    password = browser.find_element(By.NAME, "password")
    confirm_password = browser.find_element(By.NAME, "confirm_password")
    
    username.send_keys("e2e_user")
    email.send_keys("e2e@example.com")
    password.send_keys("e2e_password123")
    confirm_password.send_keys("e2e_password123")
    
    # Submete o formulário
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Verifica se foi redirecionado para a página de login
    assert "Login" in browser.title
    
    # Preenche o formulário de login
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    
    username.send_keys("e2e_user")
    password.send_keys("e2e_password123")
    
    # Submete o formulário
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Verifica se foi redirecionado para o dashboard
    assert "Dashboard" in browser.title
    
    # Verifica se o nome de usuário está sendo exibido
    assert "e2e_user" in browser.page_source

def test_add_food_entry(browser, auth_client, test_user):
    """
    Testa a adição de uma entrada de comida
    """
    # Faz login (já deve estar logado do teste anterior, mas vamos garantir)
    browser.get('http://localhost:5000/login')
    
    if "Login" in browser.title:
        username = browser.find_element(By.NAME, "username")
        password = browser.find_element(By.NAME, "password")
        
        username.send_keys("e2e_user")
        password.send_keys("e2e_password123")
        
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
    
    # Navega até a página de adicionar comida
    add_food_button = browser.find_element(By.LINK_TEXT, "Adicionar Alimento")
    add_food_button.click()
    
    # Espera o modal carregar
    time.sleep(2)  # Pequena pausa para garantir que o modal foi aberto
    
    # Seleciona um alimento da lista
    food_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-gray-100.dark\:bg-gray-700"))
    )
    food_item.click()
    
    # Preenche a quantidade
    quantity_input = browser.find_element(By.NAME, "quantity")
    quantity_input.clear()
    quantity_input.send_keys("2")
    
    # Submete o formulário
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Verifica se a mensagem de sucesso é exibida
    assert "Alimento adicionado com sucesso" in browser.page_source
    
    # Verifica se o alimento aparece na lista
    food_name = "Maçã"  # Assumindo que o primeiro alimento é Maçã
    assert food_name in browser.page_source

def test_dark_mode_toggle(browser):
    """
    Testa a alternância entre os modos claro e escuro
    """
    # Acessa o dashboard
    browser.get('http://localhost:5000/dashboard')
    
    # Verifica se o modo escuro está ativo por padrão (se o sistema estiver configurado assim)
    html = browser.find_element(By.TAG_NAME, 'html')
    initial_theme = 'dark' if 'dark' in html.get_attribute('class') else 'light'
    
    # Encontra e clica no botão de alternar tema
    theme_toggle = browser.find_element(By.CSS_SELECTOR, "button[title='Alternar tema']")
    theme_toggle.click()
    
    # Pequena pausa para a transição
    time.sleep(1)
    
    # Verifica se o tema foi alternado
    new_theme = 'light' if initial_theme == 'dark' else 'dark'
    assert new_theme in html.get_attribute('class')
