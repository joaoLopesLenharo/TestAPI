"""
Fixtures e hooks do pytest para captura automática de evidências.
"""

import pytest
import os
from selenium import webdriver
from scripts.evidence_generator import get_evidence_generator, EvidenceGenerator

# Instância global do gerador
evidence_gen: EvidenceGenerator = None

@pytest.fixture(scope="session", autouse=True)
def setup_evidence_generator():
    """Configura o gerador de evidências para a sessão de testes."""
    global evidence_gen
    evidence_gen = get_evidence_generator()
    yield
    # Gera relatório final
    evidence_gen.generate_evidence_report()

@pytest.fixture(scope="function")
def evidence_capture(request):
    """
    Fixture para captura de evidências durante testes.
    Usa automaticamente o nome do teste para identificar evidências.
    """
    test_name = request.node.name
    
    def capture_screenshot(driver, suffix=""):
        """Captura screenshot durante o teste."""
        if driver and evidence_gen:
            return evidence_gen.capture_screenshot(driver, test_name, suffix=suffix)
        return ""
    
    def start_video(driver):
        """Inicia gravação de vídeo."""
        if driver and evidence_gen:
            return evidence_gen.start_video_recording(driver, test_name)
        return False
    
    def capture_frame(driver):
        """Captura frame para vídeo."""
        if driver and evidence_gen:
            evidence_gen.capture_video_frame(driver, test_name)
    
    def stop_video(suffix=""):
        """Para gravação de vídeo."""
        if evidence_gen:
            return evidence_gen.stop_video_recording(test_name, suffix=suffix)
        return ""
    
    yield {
        'screenshot': capture_screenshot,
        'start_video': start_video,
        'capture_frame': capture_frame,
        'stop_video': stop_video
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook do pytest para capturar evidências automaticamente.
    Captura screenshot em caso de falha.
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Captura screenshot se o teste falhou
    if rep.when == "call" and rep.failed:
        # Tenta obter o driver do fixture browser
        if 'browser' in item.funcargs:
            driver = item.funcargs['browser']
            if driver and evidence_gen:
                test_name = item.name
                evidence_gen.capture_screenshot(driver, test_name, suffix="-F")
                print(f"📸 Screenshot de falha capturado para {test_name}")

@pytest.fixture(scope="function")
def browser_with_evidence(browser, evidence_capture, request):
    """
    Fixture que combina browser com captura automática de evidências.
    Inicia gravação de vídeo automaticamente para testes E2E.
    """
    test_name = request.node.name
    
    # Inicia gravação de vídeo se for teste E2E
    if 'e2e' in str(request.fspath) or 'test_user_journey' in test_name:
        evidence_capture['start_video'](browser)
    
    yield browser
    
    # Para gravação de vídeo ao final do teste
    if 'e2e' in str(request.fspath) or 'test_user_journey' in test_name:
        evidence_capture['stop_video']()

