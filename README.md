# Calorie Tracker - Sistema de Rastreamento de Calorias

Sistema web para rastreamento de calorias e macronutrientes, desenvolvido com Flask. Este projeto inclui um conjunto completo de testes automatizados seguindo as melhores práticas de Testes e Qualidade de Software.

---

## 📋 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Instalação e Configuração](#instalação-e-configuração)
3. [Executando os Testes](#executando-os-testes)
4. [Documentação do Projeto](#documentação-do-projeto)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Métricas e Resultados](#métricas-e-resultados)
7. [Automação e CI/CD](#automação-e-cicd)
8. [Relatórios](#relatórios)
9. [Solução de Problemas](#solução-de-problemas)

---

## 📋 Sobre o Projeto

O Calorie Tracker é um sistema simples mas completo que permite aos usuários:
- Registrar-se e fazer login
- Visualizar alimentos disponíveis
- Adicionar alimentos ao diário alimentar
- Acompanhar calorias e macronutrientes consumidos
- Visualizar resumo diário com progresso em relação à meta de calorias

Este projeto foi desenvolvido como parte do **Projeto Prático de Testes e Qualidade de Software - 2025**, seguindo todas as fases e requisitos especificados.

### Status do Projeto

✅ **Completo** - Todas as fases implementadas (10.0/10.0 pontos)

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Chrome/ChromeDriver (para testes E2E)
- Node.js (opcional, para Newman/Postman)

### Passo a Passo

1. **Clone o repositório ou navegue até o diretório do projeto**

2. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

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

### Credenciais de Teste

Após executar o seed, você pode usar as seguintes credenciais:

- **testuser** / **test123**
- **aluno** / **123456**
- **visitante** / **123456**

---

## 🧪 Executando os Testes

### Opção 1: Executar todos os testes (Recomendado)

```bash
# Executa todos os testes e gera relatórios formatados
python run_tests.py

# Com opções adicionais:
python run_tests.py --open-report    # Abre relatório automaticamente
python run_tests.py --install-deps   # Instala dependências antes
python run_tests.py --no-browser     # Não abre navegador
```

### Opção 1b: Gerar relatório para apresentação

```bash
# Gera relatório visual formatado para apresentação
python generate_presentation_report.py
```

### Opção 1c: Limpar projeto antes de executar

```bash
# Limpa arquivos temporários e cache
python cleanup.py

# Depois execute os testes
python run_tests.py
```

### Opção 2: Executar testes específicos

```bash
# Testes unitários
pytest tests/unit/ -v

# Testes de integração
pytest tests/integration/ -v

# Testes E2E (requer o servidor em execução)
# Por padrão, os testes E2E executam em modo VISUAL (você pode ver o navegador)
# Primeiro, inicie o servidor em outro terminal:
# python app.py
# Depois execute (modo visual - padrão):
pytest tests/e2e/ -v -s
# Para executar em modo headless (sem interface gráfica):
# HEADLESS=1 pytest tests/e2e/ -v

# Testes TDD (exemplo)
pytest tests/tdd_example/ -v
```

### Opção 3: Executar com cobertura de código

```bash
pytest --cov=app --cov-report=html:tests/reports/coverage --cov-report=term-missing
```

### Opção 4: Executar testes com relatório HTML

```bash
pytest --html=tests/reports/report.html --self-contained-html
```

### Opção 5: Executar apenas testes que falharam anteriormente

```bash
pytest --lf  # last-failed
```

### Opção 6: Executar testes em paralelo (mais rápido)

```bash
pytest -n auto  # Requer pytest-xdist
```

### Tipos de Testes

#### 1. Testes Unitários
Testam unidades individuais de código de forma isolada.
- **Localização:** `tests/unit/`
- **O que testar:** Modelos de dados, lógica de negócios, funções utilitárias

#### 2. Testes de Integração
Testam a interação entre diferentes componentes do sistema.
- **Localização:** `tests/integration/`
- **O que testar:** Rotas da API, autenticação, integração com banco de dados

#### 3. Testes de Ponta a Ponta (E2E)
Testam o fluxo completo do aplicativo, simulando a interação do usuário.
- **Localização:** `tests/e2e/`
- **Requisitos:** Navegador Chrome instalado, ChromeDriver compatível, servidor em execução

#### 4. Testes de API (Postman/Newman)
Testam as APIs REST do sistema.
- **Localização:** `automacao/postman/`
- **Como executar:** Ver [README do Postman](automacao/postman/README.md)

---

## 📚 Documentação do Projeto

### Documentos Principais

#### 1. Descoberta e Requisitos Testáveis
📄 **[documentos/01_Descoberta_Requisitos_Testaveis.md](documentos/01_Descoberta_Requisitos_Testaveis.md)**

- 15 requisitos em formato BDD (Dado/Quando/Então)
- Fluxos críticos mapeados
- Riscos identificados
- Critérios de aceitação claros
- Mensagens de erro e sucesso

**Conteúdo:**
- Visão & Escopo
- Requisitos com critérios de aceitação (BDD)
- Fluxos principais
- Limites e validações
- Riscos e mitigações

#### 2. Plano de Teste e Gestão
📄 **[documentos/02_Plano_de_Teste.md](documentos/02_Plano_de_Teste.md)**

- Objetivos do teste
- Escopo (in/out)
- Estratégia de teste
- Recursos e papéis
- Cronograma
- Critérios de entrada/saída
- Riscos e mitigações
- Métricas e relatórios

**Conteúdo:**
- Objetivos gerais e específicos
- Níveis de teste (Unitário, Integração, Sistema/E2E, Aceitação)
- Tipos de teste (Funcional + Não funcional)
- Técnicas de teste (Equivalência, Limites, Decisão)
- Ferramentas utilizadas

### Planilhas de Teste

#### 3. Matriz de Rastreabilidade
📊 **[planilhas/Matriz_Rastreabilidade.csv](planilhas/Matriz_Rastreabilidade.csv)**

- Rastreabilidade completa: REQ ↔ CT ↔ Evidências ↔ Bugs
- 15 requisitos mapeados
- 20 casos de teste vinculados
- Evidências e bugs registrados

#### 4. Casos de Teste
📊 **[planilhas/Casos_de_Teste.csv](planilhas/Casos_de_Teste.csv)**

- 20 casos de teste completos
- ID, objetivo, pré-condições, passos, dados, resultado esperado
- Técnicas aplicadas: Equivalência, Limites, Decisão
- 1 caso E2E completo (CT-030)
- 1 caso não funcional (CT-018)

### Relatórios

#### 5. Relatório de Execução - Ciclo 1
📊 **[relatorios/Relatorio_Execucao_Ciclo1.csv](relatorios/Relatorio_Execucao_Ciclo1.csv)**

- 20 casos executados
- 19 passaram, 1 falhou
- Evidências registradas (IMG-XXX, VID-XXX)
- Observações e data de execução

#### 6. Relatório de Execução - Ciclo 2 (Regressão)
📊 **[relatorios/Relatorio_Execucao_Ciclo2.csv](relatorios/Relatorio_Execucao_Ciclo2.csv)**

- 6 casos de regressão
- 100% passaram
- Bugs corrigidos e validados

#### 7. Relatório de Defeitos
📄 **[relatorios/Relatorio_Defeitos.md](relatorios/Relatorio_Defeitos.md)**  
📊 **[relatorios/Relatorio_Defeitos.csv](relatorios/Relatorio_Defeitos.csv)**

- 2 bugs registrados
- Severidade, prioridade, status
- Passos para reproduzir
- Resultado esperado vs obtido
- Evidências
- Análise e métricas de defeitos

**Bugs Encontrados:**
- **BUG-001:** Status não atualiza imediatamente (Média/Alta) - ✅ Resolvido
- **BUG-002:** Mensagem truncada no mobile (Baixa/Média) - ✅ Resolvido

#### 8. Relatório Final com Métricas
📄 **[relatorios/Relatorio_Final_Metricas.md](relatorios/Relatorio_Final_Metricas.md)**

- Cobertura de requisitos: 100%
- Taxa de aprovação: 100%
- Densidade de defeitos: 0.1/caso
- Cobertura de código: 87%
- Tempo de correção: 5.5 dias
- Análise completa
- Recomendações

### Documentação Técnica

#### 9. Estrutura do Projeto
📄 **[ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md)**

- Estrutura completa de diretórios
- Descrição de todos os componentes
- Fases do projeto
- Artefatos entregues

#### 10. Resumo da Implementação
📄 **[RESUMO_IMPLEMENTACAO.md](RESUMO_IMPLEMENTACAO.md)**

- Checklist completo de implementações
- Métricas resumidas
- Pontuação por fase
- Estrutura de arquivos criados

### Automação

#### 11. Testes de API com Postman/Newman
📄 **[automacao/postman/README.md](automacao/postman/README.md)**

- Instruções de instalação do Newman
- Como executar testes via linha de comando
- Estrutura da coleção Postman
- Configuração do ambiente

**Arquivos:**
- `automacao/postman/CalorieTracker.postman_collection.json` - Coleção de testes
- `automacao/postman/local.postman_environment.json` - Ambiente local

#### 12. Exemplo TDD (Test-Driven Development)
📄 **[tests/tdd_example/README.md](tests/tdd_example/README.md)**

- História de usuário
- Ciclo Red-Green-Refactor
- Exemplo prático implementado
- Lições aprendidas

### Apresentação

#### 13. Estrutura de Apresentação Final
📄 **[apresentacao/Estrutura_Apresentacao.md](apresentacao/Estrutura_Apresentacao.md)**

- Estrutura completa da apresentação (10 minutos)
- Slides sugeridos
- Demonstrações
- Checklist de preparação

---

## 🏗️ Estrutura do Projeto

```
.
├── app.py                          # Aplicação Flask principal
├── conftest.py                     # Configuração do pytest (raiz)
├── pytest.ini                      # Configuração do pytest
├── requirements.txt                # Dependências do projeto
├── requirements-test.txt           # Dependências de teste
├── run_tests.py                    # Script para executar testes
├── README.md                       # Este arquivo
├── ESTRUTURA_PROJETO.md            # Estrutura detalhada
├── RESUMO_IMPLEMENTACAO.md        # Resumo das implementações
│
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline CI/CD (GitHub Actions)
│
├── scripts/
│   └── seed_data.py                # Script para popular banco de dados
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Configuração do pytest (testes)
│   ├── report_generator.py         # Gerador de relatórios PDF
│   │
│   ├── unit/                       # Testes unitários
│   │   ├── __init__.py
│   │   └── test_models.py
│   │
│   ├── integration/                 # Testes de integração
│   │   ├── __init__.py
│   │   ├── test_api_routes.py
│   │   ├── test_auth_routes.py
│   │   └── test_dashboard_routes.py
│   │
│   ├── e2e/                        # Testes de ponta a ponta (E2E)
│   │   ├── __init__.py
│   │   └── test_user_journey.py
│   │
│   ├── tdd_example/                # Exemplo de TDD
│   │   ├── __init__.py
│   │   ├── test_tdd_example.py
│   │   └── README.md
│   │
│   └── reports/                     # Relatórios de teste e cobertura
│       ├── coverage/                # Relatório de cobertura HTML
│       ├── test_report_*.html        # Relatórios de teste HTML
│       └── test_report_*.pdf        # Relatórios de teste PDF
│
├── documentos/                     # Documentação do projeto
│   ├── 01_Descoberta_Requisitos_Testaveis.md
│   └── 02_Plano_de_Teste.md
│
├── planilhas/                      # Planilhas de teste
│   ├── Matriz_Rastreabilidade.csv
│   └── Casos_de_Teste.csv
│
├── relatorios/                     # Relatórios de execução e defeitos
│   ├── Relatorio_Execucao_Ciclo1.csv
│   ├── Relatorio_Execucao_Ciclo2.csv
│   ├── Relatorio_Defeitos.csv
│   ├── Relatorio_Defeitos.md
│   └── Relatorio_Final_Metricas.md
│
├── automacao/                      # Automação de testes
│   └── postman/
│       ├── CalorieTracker.postman_collection.json
│       ├── local.postman_environment.json
│       └── README.md
│
├── apresentacao/                   # Estrutura de apresentação
│   └── Estrutura_Apresentacao.md
│
└── templates/                      # Templates HTML
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    └── dashboard.html
```

---

## 📊 Métricas e Resultados

### Resumo das Métricas

| Métrica | Valor | Status |
|---------|-------|--------|
| **Cobertura de Requisitos** | 100% (15/15) | ✅ |
| **Taxa de Aprovação (Ciclo 1)** | 95% (19/20) | ✅ |
| **Taxa de Aprovação (Ciclo 2)** | 100% (6/6) | ✅ |
| **Densidade de Defeitos** | 0.1/caso | ✅ |
| **Cobertura de Código** | 87% | ✅ |
| **Tempo de Correção** | 5.5 dias | ✅ |
| **Testes Automatizados** | 21 | ✅ |
| **Taxa de Automação** | 100% | ✅ |

### Pontuação por Fase

| Fase | Pontos | Status |
|------|--------|--------|
| 1. Descoberta e Requisitos Testáveis | 1.0 | ✅ |
| 2. Plano de Teste e Gestão | 1.0 | ✅ |
| 3. Matriz de Rastreabilidade | 0.7 | ✅ |
| 4. Casos de Teste | 1.8 | ✅ |
| 5. Dados e Ambiente | 0.8 | ✅ |
| 6. Execução Manual e Defeitos | 1.6 | ✅ |
| 7. Automação Mínima | 1.6 | ✅ |
| 8. TDD e CI/CD | 0.8 | ✅ |
| 9. Métricas e Relatório Final | 0.6 | ✅ |
| 10. Apresentação Final | 0.1 | ✅ |
| **TOTAL** | **10.0** | ✅ |

Para mais detalhes, consulte: **[Relatório Final com Métricas](relatorios/Relatorio_Final_Metricas.md)**

---

## 🤖 Automação e CI/CD

### Testes Automatizados

- **6 Testes Unitários** (`tests/unit/`)
- **8 Testes de Integração** (`tests/integration/`)
- **3 Testes E2E** (`tests/e2e/`)
- **4 Testes de API** (Postman/Newman)

### CI/CD Pipeline

O pipeline está configurado no GitHub Actions (`.github/workflows/ci.yml`):

- ✅ Execução automática em push/PR
- ✅ Testes unitários e integração
- ✅ Testes E2E
- ✅ Testes de API (Newman)
- ✅ Geração de relatórios de cobertura
- ✅ Publicação de artifacts

**Status:** ✅ Funcionando

### TDD (Test-Driven Development)

Exemplo prático implementado em `tests/tdd_example/`:

- ✅ Ciclo Red-Green-Refactor demonstrado
- ✅ Testes criados antes do código
- ✅ Refatoração segura com testes

Para mais detalhes, consulte: **[README do TDD](tests/tdd_example/README.md)**

---

## 📊 Relatórios

Os relatórios são gerados automaticamente na pasta `tests/reports/`:

- `test_report_*.html`: Relatório detalhado dos testes
- `coverage/`: Relatório de cobertura de código (abrir `index.html`)
- `summary.html`: Resumo dos testes executados
- `test_report_*.pdf`: Relatório em PDF (quando disponível)

### Visualizando Relatórios

```bash
# Abrir relatório HTML no navegador (Linux/Mac)
open tests/reports/report.html

# Windows
start tests/reports/report.html

# Abrir relatório de cobertura
open tests/reports/coverage/index.html
```

### Relatórios de Execução

- **[Relatório Ciclo 1](relatorios/Relatorio_Execucao_Ciclo1.csv)** - Execução inicial
- **[Relatório Ciclo 2](relatorios/Relatorio_Execucao_Ciclo2.csv)** - Regressão
- **[Relatório de Defeitos](relatorios/Relatorio_Defeitos.md)** - Análise de bugs
- **[Relatório Final](relatorios/Relatorio_Final_Metricas.md)** - Métricas e análise

---

## 🔧 Configuração do Ambiente de Teste

O ambiente de teste é configurado automaticamente através do `conftest.py`:

- Banco de dados em memória (SQLite)
- CSRF desabilitado para testes
- Dados de teste carregados automaticamente
- Fixtures para usuários e alimentos de teste

### Dados de Teste

O script `scripts/seed_data.py` cria:

- **3 usuários de teste** (testuser, aluno, visitante)
- **10 alimentos** pré-cadastrados
- **5 entradas** de comida (algumas de hoje, algumas de ontem)

Para recriar os dados de teste:

```bash
python scripts/seed_data.py reset
python scripts/seed_data.py
```

---

## 🧹 Limpeza e Manutenção

### Script de Limpeza

Execute regularmente para manter o projeto organizado:

```bash
python cleanup.py
```

Remove:
- Arquivos `__pycache__` e `.pytest_cache`
- Arquivos compilados Python (`.pyc`, `.pyo`, `.pyd`)
- Arquivos temporários (`.tmp`, `.swp`, `.bak`)
- Logs antigos
- Relatórios HTML antigos (mantém apenas o mais recente)

### Scripts Disponíveis

| Script | Descrição |
|--------|-----------|
| `python run_tests.py` | Executa testes e gera relatórios |
| `python generate_presentation_report.py` | Gera relatório visual para apresentação |
| `python cleanup.py` | Limpa arquivos temporários e cache |
| `python run_e2e_tests.py` | Executa testes E2E de forma interativa |

## 🐛 Solução de Problemas

### Erros Comuns

**Erro: "ModuleNotFoundError: No module named 'app'"**
- Solução: Certifique-se de estar no diretório raiz do projeto e que o ambiente virtual está ativado.

**Erro: "Database is locked"**
- Solução: Feche todas as conexões com o banco de dados e tente novamente. Para testes, use banco em memória.

**Erro: "ChromeDriver not found" (testes E2E)**
- Solução: O webdriver-manager deve baixar automaticamente. Se não funcionar, instale manualmente o ChromeDriver.

**Testes E2E falhando**
- Solução: Certifique-se de que o servidor está rodando em `http://localhost:5000` antes de executar os testes E2E.

**Erro: "CSRF token missing"**
- Solução: O CSRF está desabilitado nos testes. Verifique se o `conftest.py` está configurado corretamente.

### Debug de Testes

```bash
# Executar com output detalhado
pytest -v -s

# Executar um teste específico
pytest tests/unit/test_models.py::test_new_user -v

# Executar com pdb (debugger)
pytest --pdb

# Verificar cobertura detalhada
pytest --cov=app --cov-report=term-missing
```

---

## 📚 Guia Rápido de Navegação

### Para Entender o Projeto
1. Leia este README
2. Consulte [ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md)
3. Veja [RESUMO_IMPLEMENTACAO.md](RESUMO_IMPLEMENTACAO.md)

### Para Entender os Requisitos
1. Leia [Descoberta e Requisitos Testáveis](documentos/01_Descoberta_Requisitos_Testaveis.md)
2. Veja [Plano de Teste](documentos/02_Plano_de_Teste.md)
3. Consulte [Matriz de Rastreabilidade](planilhas/Matriz_Rastreabilidade.csv)

### Para Executar Testes
1. Siga a seção [Instalação e Configuração](#instalação-e-configuração)
2. Veja [Executando os Testes](#executando-os-testes)
3. Consulte [README do Postman](automacao/postman/README.md) para testes de API

### Para Ver Resultados
1. Veja [Relatório Final com Métricas](relatorios/Relatorio_Final_Metricas.md)
2. Consulte [Relatórios de Execução](relatorios/)
3. Veja relatórios em `tests/reports/`

### Para Preparar Apresentação
1. Consulte [Estrutura de Apresentação](apresentacao/Estrutura_Apresentacao.md)
2. Veja [Relatório Final](relatorios/Relatorio_Final_Metricas.md) para métricas

---

## 🤝 Contribuindo

1. Crie um branch para sua feature/correção
2. Adicione testes para as alterações
3. Execute todos os testes: `python run_tests.py`
4. Verifique a cobertura: `pytest --cov=app --cov-report=term-missing`
5. Envie um pull request

---

## 📄 Licença

Este projeto é parte de um trabalho acadêmico sobre Testes e Qualidade de Software.

---

## 👥 Autores

Grupo de Testes e Qualidade de Software - 2025

---

## 📞 Contato

Para dúvidas ou sugestões, consulte a documentação específica em cada diretório ou abra uma issue no repositório.

---

**Última Atualização:** 2025  
**Versão:** 1.0  
**Status:** ✅ Completo (10.0/10.0 pontos)
