#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpar arquivos e pastas desnecessárias do projeto.
Remove arquivos temporários, cache e outros arquivos gerados automaticamente.
"""
import os
import shutil
import glob
import sys

# Configura encoding UTF-8 para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def remove_path(path, description):
    """Remove um caminho (arquivo ou diretório) se existir."""
    if os.path.exists(path):
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"[OK] Removido diretorio: {path} ({description})")
            else:
                os.remove(path)
                print(f"[OK] Removido arquivo: {path} ({description})")
            return True
        except Exception as e:
            print(f"[AVISO] Erro ao remover {path}: {e}")
            return False
    return False

def cleanup():
    """Executa a limpeza do projeto."""
    print("=" * 60)
    print("LIMPEZA DO PROJETO")
    print("=" * 60)
    print()
    
    removed_count = 0
    
    # Diretórios de cache Python
    print("[INFO] Removendo arquivos de cache Python...")
    cache_dirs = [
        ("__pycache__", "Cache Python"),
        (".pytest_cache", "Cache do pytest"),
        (".mypy_cache", "Cache do mypy"),
    ]
    
    for dir_name, description in cache_dirs:
        # Remove em todos os níveis
        for root, dirs, files in os.walk('.'):
            if dir_name in dirs:
                full_path = os.path.join(root, dir_name)
                if remove_path(full_path, description):
                    removed_count += 1
    
    # Arquivos .pyc, .pyo, .pyd
    print("\n[INFO] Removendo arquivos compilados Python...")
    for pattern in ['**/*.pyc', '**/*.pyo', '**/*.pyd']:
        for file_path in glob.glob(pattern, recursive=True):
            if remove_path(file_path, "Arquivo compilado Python"):
                removed_count += 1
    
    # Arquivos de cobertura antigos (mantém apenas os mais recentes)
    print("\n[INFO] Limpando relatorios de cobertura antigos...")
    coverage_files = [
        ".coverage",
        "coverage.xml",
        "htmlcov",
    ]
    for item in coverage_files:
        if remove_path(item, "Arquivo de cobertura"):
            removed_count += 1
    
    # Arquivos temporários
    print("\n[INFO] Removendo arquivos temporarios...")
    temp_patterns = ['**/*.tmp', '**/*.swp', '**/*.bak', '**/*~']
    for pattern in temp_patterns:
        for file_path in glob.glob(pattern, recursive=True):
            if remove_path(file_path, "Arquivo temporário"):
                removed_count += 1
    
    # Logs
    print("\n[INFO] Removendo arquivos de log...")
    for log_file in glob.glob('**/*.log', recursive=True):
        if remove_path(log_file, "Arquivo de log"):
            removed_count += 1
    
    # Banco de dados de teste (instance/)
    print("\n[INFO] Removendo banco de dados de teste...")
    if remove_path("instance", "Banco de dados de teste"):
        removed_count += 1
    
    # Arquivos de relatório HTML antigos (mantém apenas o mais recente)
    print("\n[INFO] Limpando relatorios HTML antigos...")
    if os.path.exists("tests/reports"):
        report_files = []
        for file in os.listdir("tests/reports"):
            if file.startswith("test_report_") and file.endswith(".html"):
                file_path = os.path.join("tests/reports", file)
                report_files.append((file_path, os.path.getmtime(file_path)))
        
        # Mantém apenas o mais recente
        if len(report_files) > 1:
            report_files.sort(key=lambda x: x[1], reverse=True)
            for file_path, _ in report_files[1:]:  # Remove todos exceto o mais recente
                if remove_path(file_path, "Relatório HTML antigo"):
                    removed_count += 1
    
    print()
    print("=" * 60)
    print(f"[SUCESSO] Limpeza concluida! {removed_count} itens removidos.")
    print("=" * 60)
    print()
    print("[DICA] Execute 'python cleanup.py' regularmente para manter o projeto limpo.")

if __name__ == "__main__":
    cleanup()

