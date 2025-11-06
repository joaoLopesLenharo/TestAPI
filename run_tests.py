#!/usr/bin/env python3
"""
Script para executar testes automatizados e gerar relatórios.
"""
import os
import sys
import subprocess
import webbrowser
from datetime import datetime

def run_tests():
    """Executa os testes e gera relatórios."""
    print("🚀 Iniciando execução dos testes...")
    
    # Cria o diretório de relatórios se não existir
    os.makedirs("tests/reports", exist_ok=True)
    
    # Gera um timestamp para os relatórios
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Comando para executar os testes
    cmd = [
        "pytest",
        "-v",
        "--cov=app",
        "--cov-report=term-missing",
        f"--html=tests/reports/test_report_{timestamp}.html",
        "--self-contained-html",
        "--cov-report=html:tests/reports/coverage"
    ]
    
    # Executa os testes
    result = subprocess.run(cmd)
    
    # Retorna o código de saída
    return result.returncode

def generate_summary():
    """Gera um resumo dos testes."""
    print("\n📊 Gerando resumo dos testes...")
    
    # Conta o número total de testes
    test_files = []
    for root, _, files in os.walk("tests"):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                test_files.append(os.path.join(root, file))
    
    # Conta o número de testes unitários, de integração e E2E
    unit_tests = len([f for f in test_files if "/unit/" in f.replace("\\", "/")])
    integration_tests = len([f for f in test_files if "/integration/" in f.replace("\\", "/")])
    e2e_tests = len([f for f in test_files if "/e2e/" in f.replace("\\", "/")])
    
    # Gera um resumo em HTML
    summary = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resumo dos Testes - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .summary {{ 
                background-color: #f5f5f5; 
                border-radius: 5px; 
                padding: 20px; 
                margin-bottom: 20px;
            }}
            .test-type {{ 
                margin: 10px 0; 
                padding: 10px; 
                border-left: 4px solid #4CAF50;
                background-color: #e8f5e9;
            }}
            .metrics {{ 
                display: flex; 
                justify-content: space-around; 
                margin: 20px 0; 
            }}
            .metric {{ 
                text-align: center; 
                padding: 10px; 
                border-radius: 5px; 
                background-color: #e3f2fd;
                flex: 1;
                margin: 0 5px;
            }}
            h1, h2 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>Resumo dos Testes</h1>
        <p>Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        
        <div class="metrics">
            <div class="metric">
                <h3>Testes Unitários</h3>
                <p>{unit_tests} arquivos</p>
            </div>
            <div class="metric">
                <h3>Testes de Integração</h3>
                <p>{integration_tests} arquivos</p>
            </div>
            <div class="metric">
                <h3>Testes E2E</h3>
                <p>{e2e_tests} arquivos</p>
            </div>
        </div>
        
        <div class="summary">
            <h2>Próximos Passos</h2>
            <p>Para visualizar os relatórios detalhados, abra os seguintes arquivos:</p>
            <ul>
                <li><strong>Relatório de Testes:</strong> tests/reports/test_report_*.html</li>
                <li><strong>Cobertura de Código:</strong> tests/reports/coverage/index.html</li>
            </ul>
        </div>
    </body>
    </html>
    """
    
    # Salva o resumo
    with open("tests/reports/summary.html", "w", encoding="utf-8") as f:
        f.write(summary)
    
    return summary

def main():
    """Função principal."""
    # Instala as dependências de teste
    print("🔧 Instalando dependências de teste...")
    subprocess.run(["pip", "install", "-r", "requirements-test.txt"])
    
    # Executa os testes
    return_code = run_tests()
    
    # Gera o resumo
    generate_summary()
    
    # Abre o relatório no navegador
    print("\n✅ Testes concluídos!")
    print("📂 Relatórios gerados em: tests/reports/")
    
    if "--no-browser" not in sys.argv:
        webbrowser.open("file://" + os.path.abspath("tests/reports/summary.html"))
    
    return return_code

if __name__ == "__main__":
    sys.exit(main())
