#!/usr/bin/env python3
"""
Script para executar testes E2E de forma visual e interativa.
Este script facilita a execução dos testes E2E com visualização do navegador.
"""
import os
import sys
import subprocess
import time

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

def main():
    """Função principal."""
    print("=" * 60)
    print("🧪 EXECUTOR DE TESTES E2E - MODO VISUAL")
    print("=" * 60)
    print()
    
    # Verifica se o servidor está rodando
    print("🔍 Verificando se o servidor Flask está rodando...")
    if not check_server_running():
        print("❌ ERRO: O servidor Flask não está rodando!")
        print()
        print("Por favor, inicie o servidor em outro terminal:")
        print("  python app.py")
        print()
        print("Ou execute este script novamente após iniciar o servidor.")
        return 1
    else:
        print("✅ Servidor Flask está rodando em http://localhost:5000")
    print()
    
    # Pergunta sobre o modo de execução
    print("Escolha o modo de execução:")
    print("  1. Modo VISUAL (padrão) - Você verá o navegador executando os testes")
    print("  2. Modo HEADLESS - Execução rápida sem interface gráfica")
    print()
    
    choice = input("Digite sua escolha (1 ou 2, padrão: 1): ").strip()
    
    if choice == "2":
        os.environ['HEADLESS'] = '1'
        print("🔍 Executando em modo HEADLESS...")
    else:
        if 'HEADLESS' in os.environ:
            del os.environ['HEADLESS']
        print("👁️  Executando em modo VISUAL...")
        print("   O navegador será aberto e você poderá acompanhar os testes!")
    print()
    
    # Pergunta sobre quais testes executar
    print("Escolha quais testes executar:")
    print("  1. Todos os testes E2E")
    print("  2. Apenas teste de registro e login")
    print("  3. Apenas teste de adicionar alimento")
    print("  4. Apenas teste de modo escuro")
    print()
    
    test_choice = input("Digite sua escolha (1-4, padrão: 1): ").strip()
    
    test_paths = {
        '1': 'tests/e2e/',
        '2': 'tests/e2e/test_user_journey.py::test_user_registration_and_login',
        '3': 'tests/e2e/test_user_journey.py::test_add_food_entry',
        '4': 'tests/e2e/test_user_journey.py::test_dark_mode_toggle'
    }
    
    test_path = test_paths.get(test_choice, 'tests/e2e/')
    
    print()
    print("=" * 60)
    print("🚀 Iniciando execução dos testes...")
    print("=" * 60)
    print()
    
    # Comando pytest
    cmd = [
        'pytest',
        test_path,
        '-v',
        '-s',  # Mostra output do print
        '--tb=short'  # Traceback curto
    ]
    
    # Executa os testes
    try:
        result = subprocess.run(cmd)
        return result.returncode
    except KeyboardInterrupt:
        print("\n\n⚠️  Execução interrompida pelo usuário.")
        return 130
    except Exception as e:
        print(f"\n❌ Erro ao executar testes: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

