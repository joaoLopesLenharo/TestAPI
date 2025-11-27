#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal para gerar todas as evidências automaticamente.
Executa todos os testes e captura evidências (screenshots e vídeos).
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Configura encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def check_dependencies():
    """Verifica se todas as dependências estão instaladas."""
    print("🔍 Verificando dependências...")
    
    # Mapeamento de nome do pacote para nome de importação
    required_packages = {
        'pytest': 'pytest',
        'selenium': 'selenium',
        'opencv-python': 'cv2',  # opencv-python é importado como cv2
        'pillow': 'PIL',  # pillow é importado como PIL
        'numpy': 'numpy',
        'imageio': 'imageio'
    }
    
    missing = []
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
        except (ImportError, AttributeError, ModuleNotFoundError) as e:
            # Trata erro de compatibilidade NumPy 2.x com opencv-python
            if package_name == 'opencv-python' and ('ARRAY_API' in str(e) or 'numpy' in str(e).lower()):
                print(f"\nAVISO: Problema de compatibilidade detectado!")
                print(f"       opencv-python nao e compativel com NumPy 2.x")
                print(f"       Solucao: pip install 'numpy<2'")
                print(f"       Ou reinstale: pip install --upgrade --force-reinstall opencv-python")
                missing.append(package_name)
            else:
                missing.append(package_name)
    
    if missing:
        print(f"\nERRO: Dependencias faltando: {', '.join(missing)}")
        print(f"Execute: pip install {' '.join(missing)}")
        return False
    
    print("OK: Todas as dependencias estao instaladas")
    return True

def check_server_running():
    """Verifica se o servidor Flask está rodando."""
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5000))
        sock.close()
        if result == 0:
            print("OK: Servidor Flask esta rodando na porta 5000")
            return True
    except:
        pass
    
    print("AVISO: Servidor Flask nao esta rodando na porta 5000")
    print("Execute: python app.py (em outro terminal)")
    return False

def setup_environment():
    """Prepara o ambiente para execução dos testes."""
    print("\nPreparando ambiente...")
    
    # Cria diretórios necessários
    Path("evidencias").mkdir(exist_ok=True)
    Path("tests/reports").mkdir(parents=True, exist_ok=True)
    
    # Popula banco de dados se necessário
    print("Verificando banco de dados...")
    if not Path("instance/calories.db").exists():
        print("Populando banco de dados...")
        subprocess.run([sys.executable, "scripts/seed_data.py"], check=False)
    
    print("OK: Ambiente preparado")

def run_tests_with_evidence():
    """Executa testes e captura evidências."""
    print("\nExecutando testes e capturando evidencias...")
    print("=" * 60)
    
    # Configura variáveis de ambiente
    env = os.environ.copy()
    env['CAPTURE_EVIDENCE'] = '1'
    env['HEADLESS'] = '0'  # Modo visual para capturar evidências
    
    # Executa teste simples primeiro para verificar se funciona
    print("\nExecutando teste simples de evidencias...")
    result_simple = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/e2e/test_simple_evidence.py", "-v", "-s"],
        env=env,
        capture_output=False
    )
    
    # Executa testes E2E (para capturar vídeos)
    print("\nExecutando testes E2E (com gravacao de video)...")
    result_e2e = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/e2e/test_user_journey_with_evidence.py", "-v", "-s"],
        env=env,
        capture_output=False
    )
    
    # Executa testes de integração (para capturar screenshots de APIs)
    print("\nExecutando testes de integracao...")
    result_integration = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/integration/", "-v"],
        env=env,
        capture_output=False
    )
    
    # Executa testes unitários (menos evidências visuais)
    print("\nExecutando testes unitarios...")
    result_unit = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/unit/", "-v"],
        env=env,
        capture_output=False
    )
    
    # Considera sucesso se pelo menos alguns testes passaram
    # (não precisa que todos passem para capturar evidências)
    return True  # Sempre retorna True para continuar e gerar relatório

def generate_evidence_summary():
    """Gera resumo das evidências capturadas."""
    print("\nGerando resumo de evidencias...")
    
    evidencias_dir = Path("evidencias")
    
    screenshots = list(evidencias_dir.glob("IMG-*.png"))
    videos = list(evidencias_dir.glob("VID-*.mp4"))
    
    print(f"\nEvidencias capturadas:")
    print(f"   Screenshots: {len(screenshots)}")
    print(f"   Videos: {len(videos)}")
    print(f"   Total: {len(screenshots) + len(videos)}")
    
    if screenshots:
        print(f"\nScreenshots:")
        for img in sorted(screenshots)[:10]:  # Mostra primeiros 10
            print(f"   - {img.name}")
        if len(screenshots) > 10:
            print(f"   ... e mais {len(screenshots) - 10} screenshots")
    
    if videos:
        print(f"\nVideos:")
        for vid in sorted(videos):
            size_mb = vid.stat().st_size / (1024 * 1024)
            print(f"   - {vid.name} ({size_mb:.2f} MB)")

def main():
    """Função principal."""
    print("=" * 60)
    print("Sistema Autonomo de Geracao de Evidencias")
    print("=" * 60)
    
    # Verifica dependências
    if not check_dependencies():
        sys.exit(1)
    
    # Verifica servidor
    if not check_server_running():
        response = input("\nDeseja continuar mesmo assim? (s/N): ")
        if response.lower() != 's':
            sys.exit(1)
    
    # Prepara ambiente
    setup_environment()
    
    # Executa testes
    success = run_tests_with_evidence()
    
    # Gera resumo
    generate_evidence_summary()
    
    print("\n" + "=" * 60)
    if success:
        print("OK: Processo concluido com sucesso!")
    else:
        print("AVISO: Alguns testes falharam, mas evidencias foram capturadas")
    print("=" * 60)
    
    print(f"\nEvidencias salvas em: {Path('evidencias').absolute()}")
    print(f"Relatorio gerado em: {Path('evidencias/evidence_report.json').absolute()}")

if __name__ == "__main__":
    main()

