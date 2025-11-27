# 🚀 Guia Rápido - Sistema de Evidências

## Instalação Rápida

```bash
# 1. Instale as dependências
pip install -r requirements-evidence.txt

# 2. Inicie o servidor Flask (em um terminal)
python app.py

# 3. Gere todas as evidências (em outro terminal)
python scripts/generate_all_evidences.py
```

## O que o Sistema Faz

✅ **Captura screenshots automaticamente** durante os testes  
✅ **Grava vídeos** dos fluxos E2E principais  
✅ **Organiza evidências** por ID de caso de teste (IMG-001, VID-003, etc.)  
✅ **Gera relatório JSON** com todas as evidências capturadas  

## Estrutura de Saída

```
evidencias/
├── IMG-001.png          # Screenshot do CT-001
├── IMG-002.png          # Screenshot do CT-002
├── VID-003.mp4          # Vídeo do CT-003
├── IMG-010-F.png        # Screenshot de falha
└── evidence_report.json # Relatório completo
```

## Uso nos Testes

### Opção 1: Testes com Evidências Prontos

```bash
pytest tests/e2e/test_user_journey_with_evidence.py -v -s
```

### Opção 2: Adicionar aos Seus Testes

```python
def test_meu_teste(browser, evidence_capture):
    # Captura screenshot
    evidence_capture['screenshot'](browser)
    
    # Grava vídeo (opcional)
    evidence_capture['start_video'](browser)
    # ... seu código ...
    evidence_capture['stop_video']()
```

## Verificar Evidências

```bash
# Lista todas as evidências
ls evidencias/

# Visualiza relatório
cat evidencias/evidence_report.json | python -m json.tool
```

## Troubleshooting

**Problema:** Vídeos não são gerados  
**Solução:** `pip install opencv-python`

**Problema:** Screenshots em branco  
**Solução:** Execute em modo visual: `export HEADLESS=0`

**Problema:** Erro de permissão  
**Solução:** `chmod 755 evidencias/`

## Documentação Completa

📄 **[scripts/README_EVIDENCE.md](scripts/README_EVIDENCE.md)**

