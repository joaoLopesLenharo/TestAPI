# Sistema Autônomo de Geração de Evidências

Sistema completo para captura automática de screenshots e vídeos durante a execução dos testes.

## 🎯 Funcionalidades

- ✅ Captura automática de screenshots durante testes E2E
- ✅ Gravação automática de vídeos dos fluxos principais
- ✅ Nomenclatura automática baseada em IDs de casos de teste (IMG-XXX, VID-XXX)
- ✅ Captura de evidências de falhas automaticamente
- ✅ Geração de relatório JSON com todas as evidências
- ✅ Integração com pytest hooks

## 📦 Instalação

### 1. Instalar Dependências

```bash
pip install -r requirements-evidence.txt
```

### 2. Verificar Dependências

```bash
python scripts/evidence_generator.py --check
```

## 🚀 Uso

### Opção 1: Gerar Todas as Evidências Automaticamente

```bash
# Terminal 1: Inicie o servidor Flask
python app.py

# Terminal 2: Execute o script de geração
python scripts/generate_all_evidences.py
```

Este script irá:
1. Verificar dependências
2. Verificar se o servidor está rodando
3. Preparar ambiente (banco de dados)
4. Executar todos os testes
5. Capturar evidências automaticamente
6. Gerar relatório final

### Opção 2: Usar nos Testes Existentes

Os testes em `tests/e2e/test_user_journey_with_evidence.py` já estão configurados para capturar evidências automaticamente.

```bash
# Execute os testes com evidências
pytest tests/e2e/test_user_journey_with_evidence.py -v -s
```

### Opção 3: Integrar com Testes Existentes

Adicione o fixture `evidence_capture` aos seus testes:

```python
def test_meu_teste(browser, evidence_capture):
    # Captura screenshot manualmente
    evidence_capture['screenshot'](browser)
    
    # Inicia gravação de vídeo
    evidence_capture['start_video'](browser)
    
    # ... seu código de teste ...
    
    # Captura frames durante o teste
    evidence_capture['capture_frame'](browser)
    
    # Para gravação de vídeo
    evidence_capture['stop_video']()
```

## 📁 Estrutura de Arquivos

```
evidencias/
├── IMG-001.png          # Screenshot do CT-001
├── IMG-002.png          # Screenshot do CT-002
├── VID-003.mp4          # Vídeo do CT-003
├── IMG-010-F.png        # Screenshot de falha do CT-010
└── evidence_report.json  # Relatório de evidências
```

## 🔧 Configuração

### Variáveis de Ambiente

- `CAPTURE_EVIDENCE=1`: Ativa captura de evidências
- `HEADLESS=0`: Modo visual (necessário para capturar evidências)

### Mapeamento de Testes

O sistema mapeia automaticamente nomes de testes para IDs de evidências:

- `test_user_registration_and_login` → `CT-003` → `IMG-003.png`, `VID-003.mp4`
- `test_add_food_entry` → `CT-008` → `IMG-008.png`, `VID-008.mp4`
- `test_login_route` → `CT-001` → `IMG-001.png`

Você pode personalizar o mapeamento editando `scripts/evidence_generator.py`.

## 📊 Relatório de Evidências

Após a execução, um relatório JSON é gerado em `evidencias/evidence_report.json`:

```json
{
  "generated_at": "2025-12-01T10:30:00",
  "total_evidences": 25,
  "evidences": [
    {
      "filename": "IMG-001.png",
      "type": "screenshot",
      "size": 123456,
      "created": "2025-12-01T10:25:00"
    },
    ...
  ]
}
```

## 🎬 Gravação de Vídeo

O sistema grava vídeos automaticamente para:
- Testes E2E completos (CT-030, CT-003, CT-008)
- Fluxos críticos definidos no código

**Configuração de vídeo:**
- FPS: 2 frames por segundo (ajustável)
- Formato: MP4
- Qualidade: Baseada nos screenshots capturados

## 📸 Captura de Screenshots

Screenshots são capturados:
- Automaticamente em pontos-chave dos testes
- Quando um teste falha (sufixo `-F`)
- Manualmente via `evidence_capture['screenshot'](browser)`

## 🔍 Troubleshooting

### Problema: Vídeos não são gerados

**Solução:** Verifique se `opencv-python` está instalado:
```bash
pip install opencv-python
```

### Problema: Screenshots em branco

**Solução:** Certifique-se de que o navegador está em modo visual (não headless):
```bash
export HEADLESS=0
```

### Problema: Erro ao salvar evidências

**Solução:** Verifique permissões de escrita no diretório `evidencias/`:
```bash
chmod 755 evidencias/
```

## 📝 Exemplos

### Exemplo 1: Teste Simples com Screenshot

```python
def test_login(browser, evidence_capture):
    browser.get('http://localhost:5000/login')
    evidence_capture['screenshot'](browser)  # Captura screenshot
    # ... resto do teste ...
```

### Exemplo 2: Teste com Vídeo

```python
def test_fluxo_completo(browser, evidence_capture):
    evidence_capture['start_video'](browser)  # Inicia gravação
    
    browser.get('http://localhost:5000/')
    evidence_capture['capture_frame'](browser)  # Captura frame
    
    # ... ações do teste ...
    evidence_capture['capture_frame'](browser)  # Mais frames
    
    evidence_capture['stop_video']()  # Para e salva vídeo
```

### Exemplo 3: Captura de Falha Automática

```python
def test_que_pode_falhar(browser, evidence_capture):
    # Se o teste falhar, screenshot será capturado automaticamente
    # com sufixo -F (ex: IMG-010-F.png)
    assert False  # Teste falha
```

## 🎯 Casos de Uso

1. **Geração Automática Completa:**
   ```bash
   python scripts/generate_all_evidences.py
   ```

2. **Executar Testes Específicos:**
   ```bash
   pytest tests/e2e/test_user_journey_with_evidence.py::test_login_valid_with_evidence -v -s
   ```

3. **Apenas Screenshots (sem vídeo):**
   ```python
   # Use evidence_capture['screenshot']() sem start_video/stop_video
   ```

## 📚 Referências

- [Selenium Screenshot](https://www.selenium.dev/documentation/webdriver/browser_manipulation/#take-screenshot)
- [OpenCV VideoWriter](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html)
- [Pytest Hooks](https://docs.pytest.org/en/stable/reference/reference.html#hooks)

