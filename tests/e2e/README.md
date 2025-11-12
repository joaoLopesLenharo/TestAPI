# Testes E2E (End-to-End) - Visuais

Este diretório contém testes de ponta a ponta (E2E) que testam o fluxo completo da aplicação usando Selenium WebDriver.

## 🎯 Características

- **Testes Visuais**: Por padrão, os testes executam com interface gráfica visível para facilitar a visualização
- **Modo Headless Opcional**: Pode ser ativado via variável de ambiente
- **Delays Visuais**: Inclui pausas para facilitar o acompanhamento visual dos testes

## 🚀 Como Executar

### Pré-requisitos

1. **Servidor Flask rodando**: Os testes E2E requerem que o servidor esteja em execução
2. **Chrome/ChromeDriver**: O Chrome deve estar instalado no sistema

### Executar em Modo Visual (Padrão)

```bash
# Terminal 1: Inicie o servidor Flask
python app.py

# Terminal 2: Execute os testes E2E (modo visual)
pytest tests/e2e/ -v -s
```

O navegador será aberto e você poderá ver os testes sendo executados em tempo real!

### Executar em Modo Headless (Sem Interface Gráfica)

```bash
# Terminal 1: Inicie o servidor Flask
python app.py

# Terminal 2: Execute os testes E2E em modo headless
HEADLESS=1 pytest tests/e2e/ -v
```

### Executar um Teste Específico

```bash
# Modo visual
pytest tests/e2e/test_user_journey.py::test_user_registration_and_login -v -s

# Modo headless
HEADLESS=1 pytest tests/e2e/test_user_journey.py::test_user_registration_and_login -v
```

## 📋 Testes Disponíveis

1. **test_user_registration_and_login**: Testa o fluxo completo de registro e login de um novo usuário
2. **test_add_food_entry**: Testa a adição de uma entrada de comida através da interface
3. **test_dark_mode_toggle**: Verifica se o modo escuro está aplicado corretamente

## ⚙️ Configuração

### Variáveis de Ambiente

- `HEADLESS`: Define se os testes devem executar em modo headless
  - `0` ou não definido: Modo visual (padrão)
  - `1`: Modo headless

### Exemplo de Uso

```bash
# Windows PowerShell
$env:HEADLESS="1"; pytest tests/e2e/ -v

# Windows CMD
set HEADLESS=1 && pytest tests/e2e/ -v

# Linux/MacOS
HEADLESS=1 pytest tests/e2e/ -v
```

## 🎨 Visualização

Quando executados em modo visual, os testes:
- Abrem o navegador Chrome maximizado
- Executam ações com delays visuais para facilitar o acompanhamento
- Mostram mensagens no console indicando cada etapa
- Mantêm o navegador aberto por alguns segundos após cada teste para visualização final

## 🔧 Troubleshooting

### Erro: "ChromeDriver not found"
- O webdriver-manager deve baixar automaticamente
- Se não funcionar, instale manualmente o ChromeDriver compatível com sua versão do Chrome

### Erro: "Connection refused"
- Certifique-se de que o servidor Flask está rodando em `http://localhost:5000`
- Verifique se a porta 5000 não está sendo usada por outro processo

### Testes muito rápidos para visualizar
- Os delays visuais são ajustados automaticamente
- Em modo visual, cada ação tem uma pausa de 1.5 segundos
- Você pode ajustar o `VISUAL_DELAY` no código se necessário

## 📝 Notas

- Os testes E2E são mais lentos que os testes unitários/integração
- Recomenda-se executar em modo visual durante o desenvolvimento
- Use modo headless em CI/CD ou quando precisar de execução rápida

