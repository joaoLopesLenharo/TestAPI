#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar testes do Postman via Newman.
Gera relatórios formatados para análise e apresentação.
"""
import os
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path

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

def check_newman_installed():
    """Verifica se o Newman está instalado."""
    try:
        result = subprocess.run(
            ["newman", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

def check_server_running():
    """Verifica se o servidor Flask está rodando."""
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5000))
        sock.close()
        return result == 0
    except:
        return False

def run_newman_tests():
    """Executa os testes do Postman via Newman."""
    print_header("EXECUTANDO TESTES POSTMAN VIA NEWMAN")
    
    # Verifica se o Newman está instalado
    if not check_newman_installed():
        print("[ERRO] Newman nao esta instalado!")
        print()
        print("[INFO] Para instalar o Newman, execute:")
        print("       npm install -g newman")
        print()
        print("[INFO] Ou instale o Node.js primeiro:")
        print("       https://nodejs.org/")
        return 1
    
    # Verifica se o servidor está rodando
    if not check_server_running():
        print("[AVISO] O servidor Flask nao parece estar rodando em http://localhost:5000")
        print("[INFO]  Inicie o servidor antes de executar os testes:")
        print("        python app.py")
        print()
        resposta = input("Deseja continuar mesmo assim? (s/N): ")
        if resposta.lower() != 's':
            return 1
    
    # Caminhos dos arquivos
    collection_path = os.path.join("automacao", "postman", "CalorieTracker.postman_collection.json")
    environment_path = os.path.join("automacao", "postman", "local.postman_environment.json")
    
    # Verifica se os arquivos existem
    if not os.path.exists(collection_path):
        print(f"[ERRO] Arquivo de colecao nao encontrado: {collection_path}")
        return 1
    
    if not os.path.exists(environment_path):
        print(f"[ERRO] Arquivo de ambiente nao encontrado: {environment_path}")
        return 1
    
    # Cria diretório de relatórios
    reports_dir = os.path.join("automacao", "postman", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    # Gera timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Comando Newman
    html_report = os.path.join(reports_dir, f"newman_report_{timestamp}.html")
    json_report = os.path.join(reports_dir, f"newman_report_{timestamp}.json")
    
    cmd = [
        "newman",
        "run", collection_path,
        "-e", environment_path,
        "-r", "html,json,cli",
        "--reporter-html-export", html_report,
        "--reporter-json-export", json_report,
        "--verbose"
    ]
    
    print("[INFO] Executando testes...")
    print(f"       Colecao: {collection_path}")
    print(f"       Ambiente: {environment_path}")
    print()
    
    # Executa o Newman
    result = subprocess.run(cmd, cwd=os.getcwd())
    
    print()
    if result.returncode == 0:
        print("[SUCESSO] Todos os testes passaram!")
    else:
        print("[AVISO] Alguns testes falharam.")
    
    print()
    print("[RELATORIOS] Relatorios gerados em:")
    print(f"             HTML: {os.path.abspath(html_report)}")
    print(f"             JSON: {os.path.abspath(json_report)}")
    print()
    
    return result.returncode

def main():
    """Função principal."""
    print_header("TESTES DE API - POSTMAN/NEWMAN")
    
    # Muda para o diretório do script se necessário
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    
    if os.path.exists(project_root):
        os.chdir(project_root)
    
    return_code = run_newman_tests()
    
    print_header("CONCLUSAO")
    
    if return_code == 0:
        print("[SUCESSO] Execucao concluida com sucesso!")
    else:
        print("[AVISO] Execucao concluida com erros.")
    
    print()
    return return_code

if __name__ == "__main__":
    sys.exit(main())

