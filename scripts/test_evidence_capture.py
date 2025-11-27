#!/usr/bin/env python3
"""
Script de teste para verificar se a captura de evidências está funcionando.
"""

import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_evidence_generator():
    """Testa o gerador de evidências diretamente."""
    print("Testando EvidenceGenerator...")
    
    try:
        from scripts.evidence_generator import EvidenceGenerator
        
        gen = EvidenceGenerator()
        print(f"OK: EvidenceGenerator criado")
        print(f"   Diretorio: {gen.base_dir.absolute()}")
        print(f"   Mapeamentos: {len(gen.test_mapping)}")
        
        # Testa captura de screenshot (sem driver real)
        print("\nTestando captura de screenshot...")
        # Não podemos testar sem um driver real, mas podemos verificar a estrutura
        
        return True
    except Exception as e:
        print(f"ERRO: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_imports():
    """Testa se todas as dependências podem ser importadas."""
    print("\nTestando imports...")
    
    dependencies = {
        'cv2': 'opencv-python',
        'PIL': 'pillow',
        'numpy': 'numpy',
        'selenium': 'selenium',
        'pytest': 'pytest'
    }
    
    missing = []
    for import_name, package_name in dependencies.items():
        try:
            __import__(import_name)
            print(f"  OK: {package_name}")
        except ImportError as e:
            print(f"  FALTA: {package_name}")
            missing.append(package_name)
    
    return len(missing) == 0

def test_directory_structure():
    """Verifica se a estrutura de diretórios está correta."""
    print("\nVerificando estrutura de diretorios...")
    
    evidencias_dir = Path("evidencias")
    evidencias_dir.mkdir(exist_ok=True)
    
    print(f"  Diretorio evidencias: {evidencias_dir.absolute()}")
    print(f"  Existe: {evidencias_dir.exists()}")
    print(f"  Pode escrever: {os.access(evidencias_dir, os.W_OK)}")
    
    # Tenta criar um arquivo de teste
    test_file = evidencias_dir / "test_write.txt"
    try:
        test_file.write_text("test")
        test_file.unlink()
        print(f"  OK: Pode escrever arquivos")
        return True
    except Exception as e:
        print(f"  ERRO: Nao pode escrever: {e}")
        return False

def main():
    """Função principal."""
    print("=" * 60)
    print("Teste do Sistema de Captura de Evidencias")
    print("=" * 60)
    
    results = []
    
    results.append(("Estrutura de diretorios", test_directory_structure()))
    results.append(("Imports", test_imports()))
    results.append(("EvidenceGenerator", test_evidence_generator()))
    
    print("\n" + "=" * 60)
    print("Resumo:")
    for name, result in results:
        status = "OK" if result else "FALHOU"
        print(f"  {name}: {status}")
    
    all_ok = all(r[1] for r in results)
    
    if all_ok:
        print("\nTudo OK! O sistema de evidencias esta pronto.")
        print("\nPara capturar evidencias, execute:")
        print("  export CAPTURE_EVIDENCE=1")
        print("  pytest tests/e2e/test_user_journey_with_evidence.py -v -s")
    else:
        print("\nAlguns testes falharam. Verifique os erros acima.")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

