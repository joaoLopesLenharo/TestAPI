#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar testes automatizados e gerar relatórios formatados.
Gera relatórios visuais e estatísticas detalhadas para análise e apresentação.
"""
import os
import sys
import subprocess
import webbrowser
from datetime import datetime

# Configura encoding UTF-8 para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def print_header(title):
    """Imprime um cabeçalho formatado."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")

def run_tests():
    """Executa os testes e gera relatórios."""
    print_header("EXECUCAO DE TESTES AUTOMATIZADOS")
    
    # Cria o diretório de relatórios se não existir
    os.makedirs("tests/reports", exist_ok=True)
    
    # Gera um timestamp para os relatórios
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("[CONFIG] Configuracao:")
    print(f"         Timestamp: {timestamp}")
    print(f"         Diretorio de relatorios: tests/reports/")
    print()
    
    # Comando para executar os testes
    cmd = [
        "pytest",
        "tests/unit/",
        "tests/integration/",
        "tests/tdd_example/",
        "-v",
        "--cov=app",
        "--cov-report=term-missing",
        "--cov-report=html:tests/reports/coverage",
        f"--html=tests/reports/test_report_{timestamp}.html",
        "--self-contained-html",
        "--tb=short"  # Traceback curto para output mais limpo
    ]
    
    print("[INFO] Executando testes...")
    print("       (Aguarde, isso pode levar alguns segundos...)\n")
    
    # Executa os testes
    result = subprocess.run(cmd)
    
    print()
    if result.returncode == 0:
        print("[SUCESSO] Todos os testes executados com sucesso!")
    else:
        print("[AVISO] Alguns testes falharam. Verifique os detalhes acima.")
    
    return result.returncode

def generate_summary():
    """Gera um resumo formatado dos testes."""
    print_header("RESUMO DOS TESTES")
    
    # Conta o número total de testes
    test_files = []
    for root, _, files in os.walk("tests"):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                test_files.append(os.path.join(root, file))
    
    # Conta o número de testes por tipo
    unit_tests = len([f for f in test_files if "/unit/" in f.replace("\\", "/")])
    integration_tests = len([f for f in test_files if "/integration/" in f.replace("\\", "/")])
    e2e_tests = len([f for f in test_files if "/e2e/" in f.replace("\\", "/")])
    tdd_tests = len([f for f in test_files if "/tdd" in f.replace("\\", "/")])
    
    total_files = len(test_files)
    
    print("[ARQUIVOS] Arquivos de Teste Encontrados:")
    print(f"           Testes Unitarios:     {unit_tests:2d} arquivo(s)")
    print(f"           Testes de Integracao: {integration_tests:2d} arquivo(s)")
    print(f"           Testes E2E:           {e2e_tests:2d} arquivo(s)")
    print(f"           Testes TDD:           {tdd_tests:2d} arquivo(s)")
    print(f"           {'-' * 50}")
    print(f"           TOTAL:                {total_files:2d} arquivo(s)")
    print()
    
    print("[RELATORIOS] Relatorios Gerados:")
    print("             Relatorio HTML:        tests/reports/test_report_*.html")
    print("             Cobertura de Codigo:   tests/reports/coverage/index.html")
    print()
    
    return {
        'unit': unit_tests,
        'integration': integration_tests,
        'e2e': e2e_tests,
        'tdd': tdd_tests,
        'total': total_files
    }

def main():
    """Função principal."""
    print_header("SISTEMA DE TESTES - CALORIE TRACKER")
    
    # Verifica se deve instalar dependências
    if "--install-deps" in sys.argv:
        print("[INFO] Instalando dependencias de teste...")
        subprocess.run(["pip", "install", "-r", "requirements-test.txt"], check=False)
        print()
    
    # Executa os testes
    return_code = run_tests()
    
    # Gera o resumo
    summary = generate_summary()
    
    # Resumo final
    print_header("CONCLUSAO")
    
    if return_code == 0:
        print("[SUCESSO] Todos os testes passaram com sucesso!")
    else:
        print("[AVISO] Alguns testes falharam. Revise os detalhes acima.")
    
    print()
    print("[RELATORIOS] Relatorios disponiveis em: tests/reports/")
    print()
    print("[DICAS]")
    print("       • Abra tests/reports/coverage/index.html para ver a cobertura detalhada")
    print("       • Execute 'python generate_presentation_report.py' para relatorio de apresentacao")
    print("       • Execute 'python cleanup.py' para limpar arquivos temporarios")
    print()
    
    # Abre o relatório no navegador (opcional)
    if "--open-report" in sys.argv or ("--no-browser" not in sys.argv and return_code == 0):
        if os.path.exists("tests/reports"):
            report_files = [f for f in os.listdir("tests/reports") if f.startswith("test_report_") and f.endswith(".html")]
            if report_files:
                latest_report = sorted(report_files)[-1]
                report_path = os.path.abspath(os.path.join("tests/reports", latest_report))
                print(f"[NAVEGADOR] Abrindo relatorio: {latest_report}")
                webbrowser.open(f"file://{report_path}")
    
    return return_code

if __name__ == "__main__":
    sys.exit(main())
