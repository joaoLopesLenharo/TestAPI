"""
Teste simples para verificar captura de evidências.
"""

import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    """Configura navegador para teste simples."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    yield driver
    
    time.sleep(1)
    driver.quit()

def test_simple_screenshot(browser, evidence_capture):
    """
    Teste simples que captura um screenshot.
    CT-999: Teste de captura de evidências
    """
    print("\nTestando captura de screenshot...")
    
    # Navega para uma página simples
    browser.get('http://localhost:5000/')
    time.sleep(2)
    
    # Captura screenshot
    result = evidence_capture['screenshot'](browser)
    
    if result:
        print(f"Screenshot capturado: {result}")
        assert os.path.exists(result), f"Screenshot nao foi criado: {result}"
        print("OK: Screenshot capturado com sucesso!")
    else:
        print("AVISO: Screenshot nao foi capturado (evidencias podem estar desabilitadas)")
        print("       Execute com: export CAPTURE_EVIDENCE=1")

def test_simple_video(browser, evidence_capture):
    """
    Teste simples que grava um vídeo.
    CT-998: Teste de gravação de vídeo
    """
    print("\nTestando gravacao de video...")
    
    # Inicia gravação
    evidence_capture['start_video'](browser)
    
    # Navega e captura frames
    browser.get('http://localhost:5000/')
    time.sleep(1)
    evidence_capture['capture_frame'](browser)
    
    browser.get('http://localhost:5000/login')
    time.sleep(1)
    evidence_capture['capture_frame'](browser)
    
    # Para gravação
    result = evidence_capture['stop_video']()
    
    if result:
        print(f"Video gravado: {result}")
        assert os.path.exists(result), f"Video nao foi criado: {result}"
        print("OK: Video gravado com sucesso!")
    else:
        print("AVISO: Video nao foi gravado (evidencias podem estar desabilitadas)")

