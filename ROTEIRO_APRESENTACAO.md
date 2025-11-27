# Roteiro de Apresentação - Processo de Testes
## Projeto Prático de Testes e Qualidade de Software - 2025

---

## 📋 Informações Gerais

**Duração:** 10-15 minutos  
**Formato:** Apresentação técnica sobre testes de software  
**Público:** Professores e avaliadores do curso  
**Foco:** Processo de testes, metodologias e resultados

---

## 🎯 Objetivos da Apresentação

1. Demonstrar conhecimento prático em testes de software
2. Apresentar o processo completo de testes implementado
3. Explicar metodologias e técnicas aplicadas
4. Exibir métricas e resultados dos testes
5. Destacar as melhores práticas de teste aplicadas

---

## 📑 Estrutura da Apresentação

### 1. Abertura e Introdução (1 minuto)

**O que falar:**
- Boas-vindas e apresentação do grupo
- Tema: "Processo de Testes - Calorie Tracker"
- Contexto: Projeto Prático de Testes e Qualidade de Software - 2025
- Objetivo: Demonstrar aplicação prática de conceitos de testes de software
- Sistema utilizado: Calorie Tracker (contexto apenas, não demonstração)

**Slides sugeridos:**
- Slide de título: "Processo de Testes de Software"
- Slide com informações do grupo e projeto

**Dica:** Mantenha a introdução breve. O foco é nos testes, não no sistema.

---

### 2. Visão Geral do Processo de Testes (2 minutos)

**O que falar:**

#### 2.1. Abordagem Adotada
- Processo estruturado seguindo as 10 fases do projeto
- Metodologia BDD (Behavior-Driven Development) para requisitos
- Pirâmide de testes: Unitário → Integração → E2E
- Automação desde o início
- Rastreabilidade completa

#### 2.2. Ferramentas Utilizadas
- **Testes Unitários e Integração:** pytest (Python)
- **Testes E2E:** Selenium WebDriver
- **Testes de API:** Postman/Newman
- **Cobertura:** pytest-cov
- **CI/CD:** GitHub Actions
- **Relatórios:** pytest-html, relatórios customizados

#### 2.3. Estrutura de Testes
```
tests/
├── unit/          # 6 testes unitários
├── integration/   # 8 testes de integração
├── e2e/           # 3 testes end-to-end
└── tdd_example/   # 4 testes TDD (exemplo)
```

**Slides sugeridos:**
- Slide com pirâmide de testes
- Slide com ferramentas utilizadas
- Slide com estrutura de diretórios

---

### 3. Fases do Processo de Testes (4 minutos)

**O que falar:**

#### 3.1. Fase 1: Descoberta e Requisitos Testáveis (1.0 ponto)

**Metodologia BDD:**
- 15 requisitos documentados em formato BDD (Dado/Quando/Então)
- Exemplo de requisito:
  ```
  Dado que sou um usuário não autenticado
  Quando acesso a página de login
  Então devo ver o formulário de login
  E devo poder inserir username e senha
  ```

**Artefatos criados:**
- Documento: `documentos/01_Descoberta_Requisitos_Testaveis.md`
- 15 requisitos mapeados
- Fluxos críticos identificados
- Riscos documentados

**Demonstração:**
- Mostrar exemplo de requisito BDD
- Exibir documento de requisitos

**Slides sugeridos:**
- Slide com exemplo de requisito BDD
- Slide com quantidade de requisitos por categoria

---

#### 3.2. Fase 2: Plano de Teste e Gestão (1.0 ponto)

**Estratégia de Testes:**
- **Níveis de Teste:**
  - Unitário: Modelos, lógica de negócios
  - Integração: APIs, banco de dados, autenticação
  - Sistema/E2E: Fluxos completos do usuário
  - Aceitação: Requisitos funcionais

- **Tipos de Teste:**
  - Funcional: Funcionalidades do sistema
  - Não funcional: Performance, segurança (básico)

- **Técnicas Aplicadas:**
  - Partição de Equivalência
  - Análise de Valor Limite
  - Tabela de Decisão

**Artefatos criados:**
- Documento: `documentos/02_Plano_de_Teste.md`
- Objetivos e escopo definidos
- Estratégia documentada
- Recursos e cronograma

**Slides sugeridos:**
- Slide com níveis de teste
- Slide com técnicas aplicadas
- Slide com estratégia de teste

---

#### 3.3. Fase 3: Matriz de Rastreabilidade (0.7 ponto)

**Rastreabilidade Completa:**
- **REQ ↔ CT:** Cada requisito vinculado a casos de teste
- **CT ↔ Evidências:** Cada caso de teste com evidências
- **Evidências ↔ Bugs:** Bugs rastreados até requisitos

**Métricas:**
- 15 requisitos mapeados
- 20 casos de teste vinculados
- 100% de rastreabilidade

**Artefatos criados:**
- Planilha: `planilhas/Matriz_Rastreabilidade.csv`
- Formato: REQ-ID | CT-ID | Evidência | Bug-ID | Status

**Demonstração:**
- Mostrar exemplo da matriz de rastreabilidade
- Explicar como um requisito é rastreado até os testes

**Slides sugeridos:**
- Slide com exemplo da matriz
- Slide destacando a importância da rastreabilidade

---

#### 3.4. Fase 4: Casos de Teste (1.8 pontos)

**Casos de Teste Criados:**
- **Total:** 20 casos de teste completos
- **Formato:** ID | Objetivo | Pré-condições | Passos | Dados | Resultado Esperado
- **Técnicas aplicadas:**
  - Partição de Equivalência: Classes válidas/inválidas
  - Valor Limite: Valores mínimos, máximos, fronteiras
  - Tabela de Decisão: Combinações de condições

**Exemplos de Casos de Teste:**

**CT-001: Login com credenciais válidas**
- Técnica: Partição de Equivalência (classe válida)
- Objetivo: Verificar autenticação bem-sucedida
- Resultado: Usuário autenticado e redirecionado

**CT-015: Adicionar alimento com quantidade zero**
- Técnica: Valor Limite (valor mínimo inválido)
- Objetivo: Verificar validação de entrada
- Resultado: Mensagem de erro apropriada

**Artefatos criados:**
- Planilha: `planilhas/Casos_de_Teste.csv`
- 1 caso E2E completo (CT-030)
- 1 caso não funcional (CT-018)

**Demonstração:**
- Mostrar exemplo de caso de teste detalhado
- Explicar técnica aplicada

**Slides sugeridos:**
- Slide com exemplo de caso de teste
- Slide com distribuição por técnica
- Slide destacando casos E2E e não funcionais

---

#### 3.5. Fase 5: Dados e Ambiente (0.8 ponto)

**Ambiente de Teste:**
- Banco de dados isolado (SQLite em memória para testes)
- Dados de teste padronizados
- Scripts de seed para popular dados

**Dados de Teste:**
- 3 usuários de teste (testuser, aluno, visitante)
- 10 alimentos pré-cadastrados
- 5 entradas de comida (dados históricos)

**Scripts Criados:**
- `scripts/seed_data.py` - Popula banco de dados
- `conftest.py` - Configuração do ambiente de teste
- Fixtures para usuários e alimentos

**Demonstração:**
- Mostrar script de seed
- Explicar isolamento do ambiente de teste

**Slides sugeridos:**
- Slide com estrutura do ambiente de teste
- Slide destacando isolamento e reproduzibilidade

---

#### 3.6. Fase 6: Execução Manual e Defeitos (1.6 pontos)

**Ciclos de Execução:**

**Ciclo 1 - Execução Inicial:**
- 20 casos de teste executados
- 19 passaram (95%)
- 1 falhou
- 2 bugs encontrados

**Ciclo 2 - Regressão:**
- 6 casos de teste executados (regressão)
- 6 passaram (100%)
- Bugs corrigidos validados

**Bugs Encontrados:**

**BUG-001: Status não atualiza imediatamente**
- Severidade: Média/Alta
- Prioridade: Alta
- Descrição: Status do dashboard não atualiza após adicionar alimento
- Status: ✅ Resolvido
- Tempo de correção: 3 dias

**BUG-002: Mensagem truncada no mobile**
- Severidade: Baixa/Média
- Prioridade: Média
- Descrição: Mensagens de erro truncadas em dispositivos móveis
- Status: ✅ Resolvido
- Tempo de correção: 2.5 dias

**Artefatos criados:**
- `relatorios/Relatorio_Execucao_Ciclo1.csv`
- `relatorios/Relatorio_Execucao_Ciclo2.csv`
- `relatorios/Relatorio_Defeitos.md`
- Evidências: Screenshots e logs

**Demonstração:**
- Mostrar relatório de execução
- Exibir relatório de defeitos
- Explicar processo de rastreamento de bugs

**Slides sugeridos:**
- Slide com resultados dos ciclos
- Slide com detalhes dos bugs
- Slide com métricas de defeitos

---

#### 3.7. Fase 7: Automação Mínima (1.6 pontos)

**Testes Automatizados:**

**Testes Unitários (6 testes):**
- Localização: `tests/unit/test_models.py`
- O que testam:
  - Criação de usuário
  - Validação de senha
  - Cálculo de calorias
  - Métodos de modelo

**Exemplo de teste unitário:**
```python
def test_new_user():
    user = User(username='test', email='test@test.com')
    user.set_password('password123')
    assert user.check_password('password123')
    assert not user.check_password('wrong')
```

**Testes de Integração (8 testes):**
- Localização: `tests/integration/`
- O que testam:
  - Rotas da API (`test_api_routes.py`)
  - Autenticação (`test_auth_routes.py`)
  - Dashboard (`test_dashboard_routes.py`)

**Exemplo de teste de integração:**
```python
def test_login_success(client, test_user):
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'test123'
    })
    assert response.status_code == 302
    assert '/dashboard' in response.location
```

**Testes E2E (3 testes):**
- Localização: `tests/e2e/test_user_journey.py`
- Ferramenta: Selenium WebDriver
- O que testam:
  - Jornada completa do usuário
  - Fluxos críticos end-to-end

**Testes de API (4 testes):**
- Ferramenta: Postman/Newman
- Localização: `automacao/postman/`
- O que testam:
  - Endpoints REST
  - Autenticação de API
  - Validações

**Métricas de Automação:**
- Total de testes automatizados: 21
- Taxa de automação: 100%
- Tempo médio de execução: ~30 segundos

**Demonstração:**
- Executar testes ao vivo: `python run_tests.py`
- Mostrar código de exemplo de cada tipo
- Exibir saída dos testes

**Slides sugeridos:**
- Slide com distribuição dos testes
- Slide com exemplo de código de teste
- Slide com métricas de automação

---

#### 3.8. Fase 8: TDD e CI/CD (0.8 ponto)

**TDD (Test-Driven Development):**

**Ciclo Red-Green-Refactor:**
1. **Red:** Escrever teste que falha
2. **Green:** Escrever código mínimo para passar
3. **Refactor:** Melhorar código mantendo testes passando

**Exemplo Prático:**
- Localização: `tests/tdd_example/`
- História: "Como usuário, quero calcular calorias totais do dia"
- Teste criado antes da implementação
- Código implementado para passar no teste
- Refatoração realizada

**CI/CD Pipeline:**

**GitHub Actions (`.github/workflows/ci.yml`):**
- Execução automática em push/PR
- Executa todos os tipos de teste:
  - Testes unitários
  - Testes de integração
  - Testes E2E
  - Testes de API (Newman)
- Gera relatórios de cobertura
- Publica artifacts

**Demonstração:**
- Mostrar arquivo de workflow
- Exibir exemplo de código TDD
- Mostrar execução do pipeline (se possível)

**Slides sugeridos:**
- Slide com ciclo TDD
- Slide com diagrama do pipeline CI/CD
- Slide com exemplo de código TDD

---

#### 3.9. Fase 9: Métricas e Relatório Final (0.6 ponto)

**Métricas Coletadas:**

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

**Análise das Métricas:**
- **Cobertura de Requisitos:** Todos os requisitos têm testes associados
- **Taxa de Aprovação:** Melhoria de 95% para 100% após correções
- **Cobertura de Código:** 87% é considerado excelente
- **Densidade de Defeitos:** Baixa (0.1/caso) indica boa qualidade
- **Tempo de Correção:** Rápido (5.5 dias) mostra processo eficiente

**Artefatos criados:**
- `relatorios/Relatorio_Final_Metricas.md`
- Análise completa das métricas
- Recomendações para melhorias

**Demonstração:**
- Abrir relatório de cobertura (`tests/reports/coverage/index.html`)
- Mostrar relatório HTML de testes
- Exibir relatório de apresentação formatado

**Slides sugeridos:**
- Slide com tabela de métricas
- Slide com gráficos de cobertura
- Slide com análise dos resultados

---

### 4. Demonstração Prática de Testes (3 minutos)

**O que demonstrar:**

#### 4.1. Execução de Testes ao Vivo

**Opção 1: Executar todos os testes**
```bash
python run_tests.py
```
- Mostrar execução dos testes
- Exibir saída no terminal
- Destacar diferentes tipos de teste sendo executados
- Mostrar tempo de execução

**Opção 2: Executar testes específicos**
```bash
# Testes unitários
pytest tests/unit/ -v

# Testes de integração
pytest tests/integration/ -v

# Com cobertura detalhada
pytest --cov=app --cov-report=term-missing
```

#### 4.2. Visualização de Relatórios

**Relatório HTML de Testes:**
- Abrir `tests/reports/test_report_*.html`
- Mostrar:
  - Resumo dos testes
  - Detalhes de cada teste
  - Tempo de execução
  - Logs e erros (se houver)

**Relatório de Cobertura:**
- Abrir `tests/reports/coverage/index.html`
- Mostrar:
  - Cobertura geral (87%)
  - Cobertura por arquivo
  - Linhas não cobertas
  - Branches não cobertas

**Relatório de Apresentação:**
- Abrir `tests/reports/presentation_report.html`
- Mostrar relatório formatado visualmente

#### 4.3. Exemplo de Código de Teste

**Mostrar exemplo real:**
- Abrir arquivo de teste (`tests/unit/test_models.py` ou `tests/integration/test_api_routes.py`)
- Explicar estrutura do teste
- Mostrar asserções
- Explicar fixtures utilizadas

**Dica:** Prepare antes da apresentação para evitar problemas técnicos.

---

### 5. Técnicas de Teste Aplicadas (1 minuto)

**O que falar:**

#### 5.1. Partição de Equivalência
- Classes válidas: Credenciais corretas, dados válidos
- Classes inválidas: Credenciais incorretas, dados inválidos
- Exemplo: CT-001 (login válido) vs CT-002 (login inválido)

#### 5.2. Análise de Valor Limite
- Valores mínimos: Quantidade = 0, quantidade = 0.1
- Valores máximos: Quantidade muito grande
- Exemplo: CT-015 (quantidade zero)

#### 5.3. Tabela de Decisão
- Combinações de condições
- Exemplo: Login com diferentes combinações de username/senha

**Slides sugeridos:**
- Slide com exemplos de cada técnica
- Slide destacando onde cada técnica foi aplicada

---

### 6. Documentação e Artefatos de Teste (1 minuto)

**O que falar:**

#### 6.1. Documentos Criados

**Documentação de Testes:**
- ✅ Descoberta e Requisitos Testáveis (15 requisitos BDD)
- ✅ Plano de Teste e Gestão
- ✅ Matriz de Rastreabilidade (CSV)
- ✅ Casos de Teste (20 casos - CSV)
- ✅ Relatórios de Execução (Ciclo 1 e 2)
- ✅ Relatório de Defeitos
- ✅ Relatório Final com Métricas

**Código de Testes:**
- ✅ 21 testes automatizados
- ✅ Scripts de automação (`run_tests.py`, `generate_presentation_report.py`)
- ✅ Configuração de ambiente (`conftest.py`)
- ✅ Pipeline CI/CD (`.github/workflows/ci.yml`)

**Estrutura de Documentos:**
```
documentos/          # Documentação do processo
planilhas/           # Matriz e casos de teste
relatorios/          # Relatórios de execução
tests/               # Código de testes
automacao/           # Testes de API
```

**Slides sugeridos:**
- Slide listando documentos principais
- Slide com estrutura de diretórios
- Slide destacando rastreabilidade

---

### 7. Lições Aprendidas e Desafios (1 minuto)

**O que falar:**

#### 7.1. Lições Aprendidas sobre Testes

**Processo:**
- Importância da rastreabilidade entre requisitos e testes
- Valor de documentar requisitos em formato BDD
- Necessidade de planejamento antes de executar testes

**Automação:**
- Benefícios de automação desde o início
- Importância de testes rápidos e confiáveis
- Valor de scripts de automação para facilitar execução

**Qualidade:**
- Benefícios do TDD para qualidade de código
- Importância de múltiplos níveis de teste
- Necessidade de métricas para acompanhar qualidade

**Documentação:**
- Valor de documentação completa
- Importância de evidências para rastreabilidade
- Necessidade de relatórios claros e objetivos

#### 7.2. Desafios Enfrentados

**Técnicos:**
- Configuração inicial do ambiente de testes
- Integração de diferentes ferramentas (pytest, Selenium, Postman)
- Configuração do pipeline CI/CD
- Geração de relatórios formatados

**Processuais:**
- Manter rastreabilidade atualizada
- Gerenciar múltiplos ciclos de execução
- Documentar bugs de forma clara

#### 7.3. Soluções Implementadas

- Scripts de automação para facilitar execução
- Documentação detalhada para referência
- Ambiente de teste isolado e reproduzível
- Relatórios visuais para apresentação
- Pipeline CI/CD para execução automática

**Slides sugeridos:**
- Slide com lições aprendidas
- Slide com desafios e soluções
- Slide destacando melhorias contínuas

---

### 8. Conclusão (1 minuto)

**O que falar:**

#### 8.1. Resumo do Processo de Testes

**Completude:**
- ✅ Todas as 10 fases completadas (10.0/10.0 pontos)
- ✅ Processo estruturado e documentado
- ✅ Metodologias aplicadas corretamente

**Qualidade:**
- ✅ 100% de cobertura de requisitos
- ✅ 100% de taxa de automação
- ✅ 87% de cobertura de código
- ✅ 100% de taxa de aprovação (ciclo 2)

**Processo:**
- ✅ Rastreabilidade completa
- ✅ Documentação completa
- ✅ Pipeline CI/CD funcionando
- ✅ Métricas coletadas e analisadas

#### 8.2. Destaques do Trabalho

1. **Processo Completo:** Todas as fases do projeto implementadas
2. **Metodologias:** BDD, TDD, múltiplas técnicas de teste
3. **Automação:** 100% de automação, 21 testes automatizados
4. **Rastreabilidade:** 100% de rastreabilidade entre requisitos e testes
5. **Qualidade:** Alta cobertura e taxa de aprovação
6. **Documentação:** Artefatos completos e bem organizados

#### 8.3. Agradecimentos
- Agradecer pela atenção
- Disponibilizar para perguntas sobre o processo de testes

**Slides sugeridos:**
- Slide de conclusão com resumo
- Slide destacando principais conquistas
- Slide de agradecimentos

---

## 🎤 Dicas para a Apresentação

### Preparação
- ✅ Testar todos os comandos antes da apresentação
- ✅ Ter relatórios gerados e abertos no navegador
- ✅ Executar testes recentemente (`python run_tests.py`)
- ✅ Ter código de testes organizado e acessível
- ✅ Preparar exemplos de código para mostrar
- ✅ Ter terminal aberto e pronto

### Durante a Apresentação
- ✅ Manter contato visual com a audiência
- ✅ Falar de forma clara e pausada
- ✅ Usar transições suaves entre tópicos
- ✅ Demonstrar conhecimento técnico sobre testes
- ✅ Estar preparado para perguntas sobre metodologias
- ✅ Focar nos testes, não no sistema

### Demonstrações
- ✅ Ter terminal aberto e pronto
- ✅ Ter navegador com relatórios abertos
- ✅ Ter código fonte de testes disponível
- ✅ Ter exemplos de casos de teste prontos
- ✅ Ter matriz de rastreabilidade acessível

### Gerenciamento de Tempo
- ⏱️ Abertura: 1 min
- ⏱️ Visão Geral: 2 min
- ⏱️ Fases do Processo: 4 min
- ⏱️ Demonstração Prática: 3 min
- ⏱️ Técnicas: 1 min
- ⏱️ Documentação: 1 min
- ⏱️ Lições/Desafios: 1 min
- ⏱️ Conclusão: 1 min
- ⏱️ **Total: ~14 minutos** (com margem para perguntas)

---

## 📊 Slides Sugeridos (Estrutura)

1. **Slide de Título**
   - "Processo de Testes de Software"
   - Nome do grupo
   - Data

2. **Visão Geral do Processo**
   - Abordagem adotada
   - Ferramentas utilizadas
   - Estrutura de testes

3. **Pirâmide de Testes**
   - Distribuição dos testes
   - Quantidade por tipo

4. **Fases do Projeto**
   - As 10 fases implementadas
   - Pontuação por fase

5. **Descoberta e Requisitos**
   - Metodologia BDD
   - Exemplo de requisito

6. **Plano de Teste**
   - Níveis de teste
   - Técnicas aplicadas

7. **Matriz de Rastreabilidade**
   - Exemplo da matriz
   - Importância da rastreabilidade

8. **Casos de Teste**
   - Exemplo detalhado
   - Técnicas aplicadas

9. **Execução e Defeitos**
   - Resultados dos ciclos
   - Bugs encontrados

10. **Automação**
    - Distribuição dos testes
    - Exemplo de código

11. **TDD e CI/CD**
    - Ciclo TDD
    - Pipeline CI/CD

12. **Métricas**
    - Tabela de métricas
    - Gráficos de cobertura

13. **Demonstração**
    - Execução de testes
    - Relatórios

14. **Técnicas de Teste**
    - Partição de Equivalência
    - Valor Limite
    - Tabela de Decisão

15. **Documentação**
    - Artefatos criados
    - Estrutura de documentos

16. **Lições Aprendidas**
    - Principais aprendizados
    - Desafios e soluções

17. **Conclusão**
    - Resumo do processo
    - Destaques

18. **Agradecimentos**
    - Obrigado pela atenção
    - Perguntas?

---

## 🔧 Comandos Úteis para Demonstração

### Executar Testes
```bash
# Todos os testes
python run_tests.py

# Testes específicos
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/e2e/ -v -s

# Com cobertura detalhada
pytest --cov=app --cov-report=html:tests/reports/coverage --cov-report=term-missing
```

### Gerar Relatórios
```bash
# Relatório para apresentação
python generate_presentation_report.py

# Relatório HTML padrão
pytest --html=tests/reports/report.html --self-contained-html
```

### Testes de API
```bash
# Com Newman (Postman CLI)
newman run automacao/postman/CalorieTracker.postman_collection.json \
  -e automacao/postman/local.postman_environment.json
```

---

## 📝 Checklist de Preparação

### Antes da Apresentação
- [ ] Testes executados recentemente (`python run_tests.py`)
- [ ] Relatórios gerados e abertos no navegador
- [ ] Terminal preparado com comandos prontos
- [ ] Slides preparados e revisados
- [ ] Código fonte de testes organizado e acessível
- [ ] Exemplos de casos de teste prontos
- [ ] Matriz de rastreabilidade acessível
- [ ] Documentos de requisitos abertos

### Durante a Apresentação
- [ ] Manter calma e confiança
- [ ] Seguir o roteiro, mas ser flexível
- [ ] Demonstrar conhecimento técnico sobre testes
- [ ] Responder perguntas com clareza
- [ ] Gerenciar tempo adequadamente
- [ ] Focar nos testes, não no sistema

### Após a Apresentação
- [ ] Agradecer pela atenção
- [ ] Disponibilizar para perguntas adicionais
- [ ] Compartilhar links/repositório se solicitado

---

## 🎯 Pontos-Chave para Destacar

1. **Processo Completo:** Todas as 10 fases implementadas (10.0/10.0)
2. **Metodologias:** BDD, TDD, múltiplas técnicas de teste aplicadas
3. **Rastreabilidade:** 100% de rastreabilidade entre requisitos e testes
4. **Automação:** 100% de taxa de automação, 21 testes automatizados
5. **Qualidade:** 100% de cobertura de requisitos, 87% de código
6. **Documentação:** Artefatos completos e bem organizados
7. **Métricas:** Coleta e análise de métricas de qualidade
8. **CI/CD:** Pipeline automatizado funcionando

---

## 📚 Referências Rápidas

### Arquivos Importantes de Testes
- `tests/unit/` - Testes unitários
- `tests/integration/` - Testes de integração
- `tests/e2e/` - Testes end-to-end
- `tests/tdd_example/` - Exemplo TDD
- `tests/reports/` - Relatórios de testes
- `documentos/` - Documentação do processo
- `planilhas/` - Matriz e casos de teste
- `relatorios/` - Relatórios de execução
- `automacao/postman/` - Testes de API

### Documentos Principais
- `documentos/01_Descoberta_Requisitos_Testaveis.md` - Requisitos BDD
- `documentos/02_Plano_de_Teste.md` - Plano de teste
- `planilhas/Matriz_Rastreabilidade.csv` - Matriz de rastreabilidade
- `planilhas/Casos_de_Teste.csv` - Casos de teste
- `relatorios/Relatorio_Final_Metricas.md` - Relatório final

---

## ✅ Boa Sorte!

Lembre-se: o foco é no **processo de testes**, não no sistema. Demonstre conhecimento sobre metodologias, técnicas, automação e métricas de teste. Seja claro, objetivo e mostre o trabalho excelente realizado!

---

**Última atualização:** 2025  
**Versão:** 2.0 - Foco em Testes
