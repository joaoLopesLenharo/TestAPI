#!/usr/bin/env python3
"""
Script para gerar relatórios formatados para apresentação.
Cria relatórios visuais e estatísticas detalhadas dos testes.
"""
import os
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path

def run_tests_and_collect_results():
    """Executa os testes e coleta os resultados."""
    print("🧪 Executando testes...")
    
    # Executa pytest com saída JSON
    cmd = [
        "pytest",
        "tests/unit/",
        "tests/integration/",
        "tests/tdd_example/",
        "-v",
        "--cov=app",
        "--cov-report=json:tests/reports/coverage.json",
        "--cov-report=html:tests/reports/coverage",
        "--cov-report=term-missing",
        "--json-report",
        "--json-report-file=tests/reports/test_results.json",
        "-q"  # Modo quiet para output mais limpo
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    return result.returncode, result.stdout, result.stderr

def parse_test_output(stdout):
    """Parseia a saída do pytest para extrair estatísticas."""
    lines = stdout.split('\n')
    stats = {
        'total': 0,
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'tests': []
    }
    
    for line in lines:
        if 'passed' in line.lower() and ('failed' in line.lower() or 'error' in line.lower()):
            # Formato: "X passed, Y failed in Zs"
            parts = line.split()
            for i, part in enumerate(parts):
                if part.isdigit():
                    if 'passed' in line.lower()[:line.lower().find(part)+20]:
                        stats['passed'] = int(part)
                    elif 'failed' in line.lower()[:line.lower().find(part)+20]:
                        stats['failed'] = int(part)
                    elif 'skipped' in line.lower()[:line.lower().find(part)+20]:
                        stats['skipped'] = int(part)
            stats['total'] = stats['passed'] + stats['failed'] + stats['skipped']
    
    return stats

def load_test_results():
    """Carrega os resultados dos testes do arquivo JSON ou parseia a saída."""
    json_path = "tests/reports/test_results.json"
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return None

def load_coverage_data():
    """Carrega os dados de cobertura."""
    json_path = "tests/reports/coverage.json"
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def generate_html_report(test_results, coverage_data, stdout=""):
    """Gera um relatório HTML formatado para apresentação."""
    
    # Calcula estatísticas
    if test_results and isinstance(test_results, dict):
        total_tests = test_results.get('summary', {}).get('total', 0)
        passed = test_results.get('summary', {}).get('passed', 0)
        failed = test_results.get('summary', {}).get('failed', 0)
        skipped = test_results.get('summary', {}).get('skipped', 0)
        
        # Estatísticas por tipo de teste
        tests_list = test_results.get('tests', [])
        unit_tests = sum(1 for t in tests_list if 'unit' in str(t.get('nodeid', '')))
        integration_tests = sum(1 for t in tests_list if 'integration' in str(t.get('nodeid', '')))
        e2e_tests = sum(1 for t in tests_list if 'e2e' in str(t.get('nodeid', '')))
        tdd_tests = sum(1 for t in tests_list if 'tdd' in str(t.get('nodeid', '')))
    else:
        # Parseia da saída do pytest
        stats = parse_test_output(stdout)
        total_tests = stats['total']
        passed = stats['passed']
        failed = stats['failed']
        skipped = stats['skipped']
        
        # Conta arquivos de teste
        unit_tests = len([f for f in os.listdir('tests/unit') if f.startswith('test_')]) if os.path.exists('tests/unit') else 0
        integration_tests = len([f for f in os.listdir('tests/integration') if f.startswith('test_')]) if os.path.exists('tests/integration') else 0
        e2e_tests = len([f for f in os.listdir('tests/e2e') if f.startswith('test_')]) if os.path.exists('tests/e2e') else 0
        tdd_tests = len([f for f in os.listdir('tests/tdd_example') if f.startswith('test_')]) if os.path.exists('tests/tdd_example') else 0
    
    # Cobertura
    if coverage_data and isinstance(coverage_data, dict):
        coverage_percent = coverage_data.get('totals', {}).get('percent_covered', 0)
    else:
        coverage_percent = 0
    
    # Taxa de aprovação
    pass_rate = (passed / total_tests * 100) if total_tests > 0 else 0
    
    # Gera HTML
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Testes - Calorie Tracker</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .content {{
            padding: 40px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        .stat-card h3 {{
            font-size: 2.5em;
            color: #667eea;
            margin-bottom: 10px;
        }}
        .stat-card p {{
            font-size: 1.1em;
            color: #666;
        }}
        .stat-card.success {{
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        }}
        .stat-card.warning {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        }}
        .stat-card.danger {{
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        }}
        .section {{
            margin-bottom: 40px;
        }}
        .section h2 {{
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        .test-types {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        .test-type-card {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #667eea;
        }}
        .test-type-card h4 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        .test-type-card .count {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .progress-bar {{
            background: #e0e0e0;
            border-radius: 10px;
            height: 30px;
            margin: 20px 0;
            overflow: hidden;
        }}
        .progress-fill {{
            background: linear-gradient(90deg, #84fab0 0%, #8fd3f4 100%);
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            transition: width 1s ease;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            margin: 5px;
        }}
        .badge-success {{
            background: #84fab0;
            color: #2d5016;
        }}
        .badge-danger {{
            background: #ff9a9e;
            color: #8b0000;
        }}
        .badge-info {{
            background: #8fd3f4;
            color: #003d5c;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Relatório de Testes</h1>
            <p>Calorie Tracker - Sistema de Rastreamento de Calorias</p>
            <p style="margin-top: 10px; font-size: 0.9em;">Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📈 Estatísticas Gerais</h2>
                <div class="stats-grid">
                    <div class="stat-card success">
                        <h3>{total_tests}</h3>
                        <p>Total de Testes</p>
                    </div>
                    <div class="stat-card success">
                        <h3>{passed}</h3>
                        <p>Testes Passando</p>
                    </div>
                    <div class="stat-card {'danger' if failed > 0 else 'success'}">
                        <h3>{failed}</h3>
                        <p>Testes Falhando</p>
                    </div>
                    <div class="stat-card {'warning' if skipped > 0 else 'success'}">
                        <h3>{skipped}</h3>
                        <p>Testes Pulados</p>
                    </div>
                </div>
                
                <div class="section">
                    <h3>Taxa de Aprovação</h3>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {pass_rate}%">
                            {pass_rate:.1f}%
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🧪 Tipos de Teste</h2>
                <div class="test-types">
                    <div class="test-type-card">
                        <h4>Testes Unitários</h4>
                        <div class="count">{unit_tests}</div>
                        <span class="badge badge-info">Unit</span>
                    </div>
                    <div class="test-type-card">
                        <h4>Testes de Integração</h4>
                        <div class="count">{integration_tests}</div>
                        <span class="badge badge-info">Integration</span>
                    </div>
                    <div class="test-type-card">
                        <h4>Testes E2E</h4>
                        <div class="count">{e2e_tests}</div>
                        <span class="badge badge-info">E2E</span>
                    </div>
                    <div class="test-type-card">
                        <h4>Testes TDD</h4>
                        <div class="count">{tdd_tests}</div>
                        <span class="badge badge-info">TDD</span>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>📊 Cobertura de Código</h2>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {coverage_percent}%">
                        {coverage_percent:.1f}%
                    </div>
                </div>
                <p style="margin-top: 10px; color: #666;">
                    {coverage_percent:.1f}% do código está coberto por testes
                </p>
            </div>
            
            <div class="section">
                <h2>✅ Resumo</h2>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px;">
                    <p style="font-size: 1.1em; margin-bottom: 10px;">
                        <strong>Status Geral:</strong> 
                        <span class="badge {'badge-success' if failed == 0 else 'badge-danger'}">
                            {'✅ Todos os testes passando!' if failed == 0 else '❌ Alguns testes falharam'}
                        </span>
                    </p>
                    <p style="font-size: 1.1em; margin-bottom: 10px;">
                        <strong>Taxa de Aprovação:</strong> {pass_rate:.1f}%
                    </p>
                    <p style="font-size: 1.1em;">
                        <strong>Cobertura de Código:</strong> {coverage_percent:.1f}%
                    </p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Relatório gerado automaticamente pelo sistema de testes</p>
            <p style="margin-top: 5px; font-size: 0.9em;">
                Para mais detalhes, consulte os relatórios em <code>tests/reports/</code>
            </p>
        </div>
    </div>
</body>
</html>"""
    
    return html

def main():
    """Função principal."""
    print_header("GERADOR DE RELATORIO PARA APRESENTACAO")
    
    # Cria diretório de relatórios
    os.makedirs("tests/reports", exist_ok=True)
    
    # Executa testes
    return_code, stdout, stderr = run_tests_and_collect_results()
    
    # Carrega resultados
    print_header("COLETANDO RESULTADOS")
    test_results = load_test_results()
    coverage_data = load_coverage_data()
    
    # Gera relatório HTML
    print("[INFO] Gerando relatorio HTML...")
    html = generate_html_report(test_results, coverage_data, stdout)
    
    # Salva relatório
    report_path = "tests/reports/presentation_report.html"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print_header("RELATORIO GERADO COM SUCESSO")
    print(f"[ARQUIVO] Relatorio disponivel em:")
    print(f"          {os.path.abspath(report_path)}")
    print()
    print("[DICA] Abra o arquivo no navegador para visualizar o relatorio formatado.")
    print()
    
    return return_code

if __name__ == "__main__":
    sys.exit(main())

