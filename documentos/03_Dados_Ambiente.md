# E) Dados e Ambiente (0,8)

## Stack Tecnológica

### Backend
- **Framework:** Flask 2.3+
- **Linguagem:** Python 3.11+
- **ORM:** SQLAlchemy
- **Autenticação:** Flask-Login
- **Formulários:** Flask-WTF, WTForms

### Banco de Dados
- **SGBD:** SQLite
- **Arquivo:** `instance/calories.db`
- **Migrations:** Alembic (opcional)

### Frontend
- **Templates:** Jinja2 (HTML)
- **Estilização:** CSS (modo escuro/claro)
- **JavaScript:** Vanilla JS (fetch API)

### Testes
- **Framework:** pytest
- **E2E:** Selenium WebDriver
- **API:** Postman/Newman
- **Cobertura:** pytest-cov

## Configuração do Ambiente

### Pré-requisitos

```bash
# Python 3.11 ou superior
python --version

# pip atualizado
pip install --upgrade pip

# Chrome/ChromeDriver (para testes E2E)
# Instalado automaticamente via webdriver_manager
```

### Instalação Passo a Passo

1. **Clone o repositório ou navegue até o diretório:**
   ```bash
   cd "F:\codes\python\Trabalho testes de software"
   ```

2. **Crie e ative ambiente virtual (recomendado):**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale dependências:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-test.txt
   ```

4. **Configure o banco de dados:**
   ```bash
   # Popula o banco com dados de teste
   python scripts/seed_data.py
   
   # Para resetar o banco (limpa e recria)
   python scripts/seed_data.py reset
   ```

5. **Execute o servidor:**
   ```bash
   python app.py
   ```
   
   O servidor estará disponível em `http://localhost:5000`

## Massa de Dados (Seed)

### Usuários Criados

| Username | Email | Senha | Meta Diária (cal) |
|----------|-------|-------|-------------------|
| testuser | test@example.com | test123 | 2000 |
| aluno | aluno@uni.br | 123456 | 2500 |
| visitante | visitante@uni.br | 123456 | 1800 |

### Alimentos Criados

| Nome | Calorias | Proteínas | Carboidratos | Gorduras | Público |
|------|----------|-----------|--------------|----------|---------|
| Maçã | 52 | 0.3 | 14 | 0.2 | Sim |
| Frango Grelhado | 165 | 31 | 0 | 3.6 | Sim |
| Arroz Branco | 130 | 2.7 | 28 | 0.3 | Sim |
| Feijão Preto | 127 | 8.8 | 22.8 | 0.5 | Sim |
| Ovo Cozido | 155 | 13 | 1.1 | 11 | Sim |
| Banana | 89 | 1.1 | 23 | 0.3 | Sim |
| Pão Integral | 247 | 13 | 41 | 4.2 | Sim |
| Iogurte Natural | 59 | 10 | 3.6 | 0.4 | Sim |
| Salada Verde | 15 | 1.2 | 3 | 0.2 | Sim |
| Peito de Peru | 135 | 30 | 0 | 1 | Sim |

### Entradas de Teste

- **testuser:** 2x Maçã, 1x Frango Grelhado (hoje)
- **testuser:** 1x Arroz Branco (ontem)
- **aluno:** 1x Feijão Preto, 2x Ovo Cozido (hoje)

## IDs Estáveis (data-testid)

Para facilitar testes automatizados, os seguintes elementos possuem identificadores estáveis:

### Autenticação
- `data-testid="login-username"` - Campo de username no login
- `data-testid="login-password"` - Campo de senha no login
- `data-testid="btn-login"` - Botão de login
- `data-testid="btn-register"` - Botão de registro

### Dashboard
- `data-testid="dashboard-calories"` - Total de calorias
- `data-testid="dashboard-protein"` - Total de proteínas
- `data-testid="dashboard-carbs"` - Total de carboidratos
- `data-testid="dashboard-fat"` - Total de gorduras
- `data-testid="btn-add-food"` - Botão adicionar alimento
- `data-testid="food-modal"` - Modal de adicionar alimento

### API Endpoints

- `POST /login` - Autenticação
- `GET /api/food` - Listar alimentos
- `POST /api/entry` - Adicionar entrada
- `GET /dashboard` - Dashboard (requer autenticação)

## Script de Reset

Para garantir consistência entre ciclos de teste:

```bash
# Reset completo (limpa e recria banco)
python scripts/seed_data.py reset

# Seed com dados de teste
python scripts/seed_data.py
```

**Uso:** Execute antes de cada ciclo de teste para garantir dados limpos e consistentes.

## Variáveis de Ambiente

### Desenvolvimento
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///calories.db
```

### Testes
```env
FLASK_ENV=testing
TESTING=True
SQLALCHEMY_DATABASE_URI=sqlite:///test_calories.db
```

## Credenciais de Teste

Após executar o seed, use as seguintes credenciais:

### Login Válido
- **Username:** `aluno`
- **Password:** `123456`

### Login Inválido (para testes)
- **Username:** `inexistente`
- **Password:** `qualquer`

## Cenários de Teste

### Cenário 1: Base Limpa
```bash
python scripts/seed_data.py reset
# Banco vazio, sem usuários ou alimentos
```

### Cenário 2: Base Populada (Padrão)
```bash
python scripts/seed_data.py
# 3 usuários, 10 alimentos, algumas entradas
```

### Cenário 3: Lista Vazia de Alimentos
```bash
python scripts/seed_data.py reset
# Criar apenas usuários, sem alimentos
```

### Cenário 4: Lista Vazia de Entradas
```bash
python scripts/seed_data.py
# Remover entradas manualmente ou usar usuário sem entradas
```

## Troubleshooting

### Problema: Banco de dados não encontrado
**Solução:** Execute `python scripts/seed_data.py` para criar o banco.

### Problema: Erro de permissão
**Solução:** Verifique permissões de escrita no diretório `instance/`.

### Problema: Dados inconsistentes
**Solução:** Execute `python scripts/seed_data.py reset` para resetar.

### Problema: Porta 5000 já em uso
**Solução:** Altere a porta em `app.py` ou encerre o processo que está usando a porta.

## Estrutura de Diretórios

```
Trabalho testes de software/
├── app.py                    # Aplicação Flask principal
├── scripts/
│   └── seed_data.py          # Script de seed/reset
├── instance/
│   └── calories.db           # Banco de dados SQLite
├── tests/                    # Testes automatizados
├── automacao/                # Scripts de automação
├── relatorios/               # Relatórios gerados
├── evidencias/               # Evidências (prints/vídeos)
└── documentos/               # Documentação
```

