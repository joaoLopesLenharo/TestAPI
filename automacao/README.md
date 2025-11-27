# Automação de Testes - Calorie Tracker

Este diretório contém os scripts e configurações para automação de testes do sistema Calorie Tracker.

## Estrutura

```
automacao/
├── postman/
│   ├── CalorieTracker.postman_collection.json  # Coleção de testes API
│   ├── local.postman_environment.json          # Ambiente local
│   ├── run_postman_tests.py                     # Script de execução
│   └── README.md                                 # Documentação Postman
└── README.md                                     # Este arquivo
```

## Pré-requisitos

### Para Testes E2E (Selenium)
- Python 3.11+
- Chrome/ChromeDriver instalado
- Dependências: `pip install -r requirements-test.txt`

### Para Testes API (Postman/Newman)
- Node.js instalado
- Newman CLI: `npm install -g newman`

## Executando Testes Automatizados

### 1. Testes Unitários e de Integração

```bash
# Executar todos os testes (unit + integration)
pytest tests/

# Executar apenas testes unitários
pytest tests/unit/

# Executar apenas testes de integração
pytest tests/integration/

# Com cobertura
pytest --cov=app --cov-report=html tests/
```

### 2. Testes E2E (Selenium)

```bash
# Executar testes E2E (modo visual)
pytest tests/e2e/test_user_journey.py

# Executar testes E2E (modo headless)
HEADLESS=1 pytest tests/e2e/test_user_journey.py

# Executar script específico
python run_e2e_tests.py
```

**Nota:** Certifique-se de que o servidor Flask está rodando em `http://localhost:5000` antes de executar os testes E2E.

### 3. Testes API (Postman/Newman)

```bash
# Executar coleção Postman via Newman
cd automacao/postman
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json

# Com relatório HTML
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json -r html

# Executar script Python
python run_postman_tests.py
```

### 4. Executar Todos os Testes

```bash
# Script principal
python run_tests.py

# Ou manualmente
pytest tests/ && newman run automacao/postman/CalorieTracker.postman_collection.json -e automacao/postman/local.postman_environment.json
```

## Configuração do Ambiente

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (opcional):

```env
FLASK_ENV=testing
DATABASE_URL=sqlite:///test_calories.db
SECRET_KEY=test-secret-key
```

### Setup do Banco de Dados

```bash
# Popular banco com dados de teste
python scripts/seed_data.py

# Resetar banco
python scripts/seed_data.py reset
```

## Testes Implementados

### Testes Unitários (`tests/unit/`)
- ✅ Criação de usuário
- ✅ Validação de senha
- ✅ Criação de FoodItem
- ✅ Criação de FoodEntry
- ✅ Cálculo de calorias consumidas
- ✅ Cálculo de calorias restantes

### Testes de Integração (`tests/integration/`)
- ✅ Registro de usuário
- ✅ Login válido/inválido
- ✅ Logout
- ✅ APIs REST (GET/POST)

### Testes E2E (`tests/e2e/`)
- ✅ Registro e login de novo usuário
- ✅ Adição de entrada de comida
- ✅ Verificação de modo escuro

### Testes API (Postman)
- ✅ POST /login (200/401)
- ✅ GET /api/food (lista)
- ✅ POST /api/entry (criar entrada)
- ✅ Validações de erro (400, 403, 404)

## CI/CD

### GitHub Actions

O projeto inclui um workflow do GitHub Actions (`.github/workflows/tests.yml`) que:

1. Instala dependências
2. Executa linting
3. Executa testes unitários
4. Executa testes de integração
5. Executa testes E2E (headless)
6. Executa testes Postman (Newman)
7. Gera relatório de cobertura
8. Publica artifacts

**Status:** ✅ Configurado e funcionando

## Relatórios

### Cobertura de Código
```bash
pytest --cov=app --cov-report=html tests/
# Abrir: tests/reports/coverage/index.html
```

### Relatórios de Teste
- **HTML:** `tests/reports/test_report_*.html`
- **Texto:** `tests/reports/summary_*.txt`
- **Postman:** `automacao/postman/reports/`

## Troubleshooting

### Problemas Comuns

1. **ChromeDriver não encontrado**
   - Solução: O projeto usa `webdriver_manager` que baixa automaticamente
   - Se persistir: Instale ChromeDriver manualmente

2. **Servidor Flask não está rodando**
   - Solução: Execute `python app.py` antes dos testes E2E
   - Ou use `pytest` com fixtures que iniciam o servidor

3. **Erro de autenticação nos testes**
   - Solução: Execute `python scripts/seed_data.py` para criar usuários de teste
   - Credenciais: `testuser/test123` ou `aluno/123456`

4. **Newman não encontrado**
   - Solução: `npm install -g newman`
   - Verifique: `newman --version`

## Próximos Passos

- [ ] Adicionar mais testes de API
- [ ] Implementar testes de performance (Locust)
- [ ] Adicionar testes de acessibilidade (axe-core)
- [ ] Expandir cobertura de código para 90%+

## Referências

- [pytest Documentation](https://docs.pytest.org/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Postman/Newman Documentation](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

