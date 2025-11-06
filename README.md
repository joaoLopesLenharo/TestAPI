# Sistema de Testes Automatizados - Calorie Tracker

Este documento descreve como configurar e executar os testes automatizados para o sistema Calorie Tracker.

## Estrutura de Diretórios

```
tests/
├── unit/               # Testes unitários
├── integration/        # Testes de integração
├── e2e/                # Testes de ponta a ponta (E2E)
├── utils/              # Utilitários para testes
└── reports/            # Relatórios de teste e cobertura
```

## Configuração do Ambiente

1. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-test.txt
   ```

## Executando os Testes

### Opção 1: Executar todos os testes

```bash
# Executa todos os testes e gera relatórios
python run_tests.py
```

### Opção 2: Executar testes específicos

```bash
# Testes unitários
pytest tests/unit/

# Testes de integração
pytest tests/integration/

# Testes E2E (requer o servidor em execução)
pytest tests/e2e/
```

### Opção 3: Executar com cobertura de código

```bash
pytest --cov=app --cov-report=html:tests/reports/coverage
```

## Tipos de Testes

### 1. Testes Unitários

Testam unidades individuais de código de forma isolada.

- **O que testar:**
  - Modelos de dados
  - Lógica de negócios
  - Funções utilitárias

### 2. Testes de Integração

Testam a interação entre diferentes componentes do sistema.

- **O que testar:**
  - Rotas da API
  - Autenticação
  - Integração com banco de dados

### 3. Testes de Ponta a Ponta (E2E)

Testam o fluxo completo do aplicativo, simulando a interação do usuário.

- **Requisitos:**
  - Navegador Chrome instalado
  - ChromeDriver compatível
  - Servidor em execução

## Relatórios

Os relatórios são gerados automaticamente na pasta `tests/reports/`:

- `test_report_*.html`: Relatório detalhado dos testes
- `coverage/`: Relatório de cobertura de código
- `summary.html`: Resumo dos testes executados

## Boas Práticas

1. **Nomes Descritivos:** Use nomes que descrevam o comportamento esperado.
2. **Testes Isolados:** Cada teste deve ser independente dos outros.
3. **Arrange-Act-Assert:** Estruture os testes em 3 fases claras.
4. **Mocks e Fixtures:** Use para isolar dependências externas.
5. **Cobertura de Código:** Almeje pelo menos 80% de cobertura.

## Solução de Problemas

- **Erros de Conexão:** Verifique se o servidor está em execução para testes E2E.
- **Falhas nos Testes:** Execute com `-v` para mais detalhes.
- **Problemas de Configuração:** Verifique se todas as dependências estão instaladas.

## Contribuindo

1. Crie um branch para sua feature/correção
2. Adicione testes para as alterações
3. Execute todos os testes
4. Envie um pull request
