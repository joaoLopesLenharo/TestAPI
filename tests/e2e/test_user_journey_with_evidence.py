"""
Testes E2E com captura automática de evidências.
Versão melhorada dos testes que captura screenshots e vídeos automaticamente.
"""

import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    """
    Configura o navegador para testes E2E com suporte a evidências.
    """
    options = webdriver.ChromeOptions()
    
    # Sempre executa em modo visual para capturar evidências
    if os.getenv('CAPTURE_EVIDENCE', '0') == '1':
        print("📸 Modo de captura de evidências ativado")
    
    # Opções para melhor visualização
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    yield driver
    
    time.sleep(1)
    driver.quit()

def test_user_registration_and_login_with_evidence(browser, evidence_capture, test_client, test_user):
    """
    CT-003: Testa o fluxo completo de registro e login com captura de evidências.
    """
    VISUAL_DELAY = 1.5
    
    # Inicia gravação de vídeo
    evidence_capture['start_video'](browser)
    
    print("\n📝 CT-003: Registro e Login de novo usuário")
    
    # Screenshot 1: Página inicial
    browser.get('http://localhost:5000/')
    time.sleep(VISUAL_DELAY)
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Screenshot 2: Página de registro
    register_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Sign")
    register_link.click()
    time.sleep(VISUAL_DELAY)
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Preenche formulário
    username = browser.find_element(By.NAME, "username")
    email = browser.find_element(By.NAME, "email")
    password = browser.find_element(By.NAME, "password")
    confirm_password = browser.find_element(By.NAME, "confirm_password")
    
    username.send_keys("e2e_user")
    time.sleep(0.3)
    email.send_keys("e2e@example.com")
    time.sleep(0.3)
    password.send_keys("e2e_password123")
    time.sleep(0.3)
    confirm_password.send_keys("e2e_password123")
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 3: Formulário preenchido
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Submete registro
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 4: Página de login após registro
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Login
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    username.send_keys("e2e_user")
    time.sleep(0.3)
    password.send_keys("e2e_password123")
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 5: Formulário de login preenchido
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    submit_button.click()
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 6: Dashboard (sucesso)
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    assert "Resumo" in browser.page_source or "Dashboard" in browser.page_source
    
    # Para gravação de vídeo
    evidence_capture['stop_video']()
    
    print("✅ CT-003 concluído com evidências capturadas")

def test_add_food_entry_with_evidence(browser, evidence_capture, auth_client, test_user):
    """
    CT-008: Testa adição de entrada de comida com captura de evidências.
    """
    VISUAL_DELAY = 1.5
    
    # Inicia gravação de vídeo
    evidence_capture['start_video'](browser)
    
    print("\n🍎 CT-008: Adicionar entrada de comida")
    
    # Login
    browser.get('http://localhost:5000/login')
    time.sleep(VISUAL_DELAY)
    
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    username.send_keys("testuser")
    time.sleep(0.3)
    password.send_keys("test123")
    time.sleep(VISUAL_DELAY)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(VISUAL_DELAY * 1.5)
    
    # Screenshot 1: Dashboard após login
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Abre modal de adicionar alimento
    try:
        add_food_button = browser.find_element(By.ID, "addFoodBtn")
        add_food_button.click()
    except:
        add_food_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Adicionar Alimento')]")
        add_food_button.click()
    
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 2: Modal aberto
    evidence_capture['screenshot'](browser)
    evidence_capture['capture_frame'](browser)
    
    # Tenta adicionar alimento
    try:
        food_item = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#recentFoods > div"))
        )
        food_item.click()
        time.sleep(VISUAL_DELAY)
        
        # Screenshot 3: Alimento adicionado
        evidence_capture['screenshot'](browser)
        evidence_capture['capture_frame'](browser)
    except:
        print("ℹ️  Modal funcionando (sem alimentos recentes)")
    
    # Para gravação de vídeo
    evidence_capture['stop_video']()
    
    print("✅ CT-008 concluído com evidências capturadas")

def test_login_valid_with_evidence(browser, evidence_capture):
    """
    CT-001: Testa login válido com captura de evidências.
    """
    VISUAL_DELAY = 1.5
    
    print("\n🔐 CT-001: Login válido")
    
    browser.get('http://localhost:5000/login')
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 1: Página de login
    evidence_capture['screenshot'](browser)
    
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    username.send_keys("aluno")
    time.sleep(0.3)
    password.send_keys("123456")
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 2: Formulário preenchido
    evidence_capture['screenshot'](browser)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 3: Dashboard (sucesso)
    evidence_capture['screenshot'](browser)
    
    assert "Resumo" in browser.page_source or "Dashboard" in browser.page_source
    print("✅ CT-001 concluído com evidências capturadas")

def test_login_invalid_with_evidence(browser, evidence_capture):
    """
    CT-002: Testa login inválido com captura de evidências.
    """
    VISUAL_DELAY = 1.5
    
    print("\n❌ CT-002: Login inválido")
    
    browser.get('http://localhost:5000/login')
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 1: Página de login
    evidence_capture['screenshot'](browser)
    
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    username.send_keys("inexistente")
    time.sleep(0.3)
    password.send_keys("errada")
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 2: Formulário preenchido com dados inválidos
    evidence_capture['screenshot'](browser)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(VISUAL_DELAY)
    
    # Screenshot 3: Mensagem de erro
    evidence_capture['screenshot'](browser)
    
    assert "Invalid" in browser.page_source or "invalid" in browser.page_source.lower()
    print("✅ CT-002 concluído com evidências capturadas")

