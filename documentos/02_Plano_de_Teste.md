# B) Plano de Teste e Gestão (1,0)

## 1. Objetivos do Teste

### Objetivos Gerais
Validar que o sistema Calorie Tracker atende aos requisitos funcionais e não funcionais especificados, garantindo qualidade, confiabilidade e usabilidade adequadas.

### Objetivos Específicos
- Verificar autenticação (login válido/inválido, registro, logout)
- Validar regras de negócio (cálculo de calorias, acesso a alimentos privados)
- Testar mensagens de erro/sucesso e validações
- Validar limites e casos extremos (quantidade <= 0, listas vazias)
- Verificar usabilidade básica (clareza de mensagens, tempo de resposta < 2s)
- Garantir integridade dos dados (cálculos corretos, consistência)

## 2. Escopo

### Dentro do Escopo (IN)
- ✅ Autenticação (login, registro, logout)
- ✅ Listagem de alimentos (públicos e privados)
- ✅ Adição de entradas ao diário
- ✅ Cálculo de calorias e macronutrientes
- ✅ Dashboard e visualização de resumo
- ✅ Validações de campos obrigatórios
- ✅ Proteção de rotas autenticadas
- ✅ APIs REST (GET/POST)
- ✅ Mensagens de erro/sucesso
- ✅ Casos limite (quantidade, listas vazias)

### Fora do Escopo (OUT)
- ❌ Testes de segurança avançados (SQL injection, XSS)
- ❌ Testes de carga e stress
- ❌ Testes de acessibilidade completos (WCAG)
- ❌ Testes de compatibilidade entre navegadores
- ❌ Testes de integração com sistemas externos
- ❌ Testes de backup e recuperação

## 3. Níveis de Teste

### 3.1 Teste Unitário
- **Objetivo:** Validar lógica de negócio dos modelos (User, FoodItem, FoodEntry)
- **Cobertura:** Métodos de cálculo, validações, relacionamentos
- **Ferramenta:** pytest
- **Localização:** `tests/unit/`

### 3.2 Teste de Integração
- **Objetivo:** Validar integração entre componentes (rotas, APIs, banco de dados)
- **Cobertura:** Fluxos de autenticação, APIs REST, persistência de dados
- **Ferramenta:** pytest + Flask test client
- **Localização:** `tests/integration/`

### 3.3 Teste de Sistema/E2E
- **Objetivo:** Validar fluxos completos do ponto de vista do usuário
- **Cobertura:** Fluxos críticos end-to-end (registro → login → adicionar → dashboard)
- **Ferramenta:** Selenium WebDriver
- **Localização:** `tests/e2e/`

### 3.4 Teste de Aceitação
- **Objetivo:** Validar critérios de aceitação definidos nos requisitos
- **Cobertura:** Todos os requisitos REQ-001 a REQ-018
- **Ferramenta:** Testes manuais + automação E2E
- **Critérios:** 100% dos requisitos críticos cobertos

## 4. Tipos de Teste

### 4.1 Funcional
- Autenticação e autorização
- CRUD de alimentos e entradas
- Cálculos e regras de negócio
- Validações e mensagens

### 4.2 Não Funcional
- **Usabilidade:** Clareza de mensagens, tempo de resposta
- **Performance:** Tempo de resposta < 2s (ambiente local)
- **Confiabilidade:** Tratamento de erros, consistência de dados

## 5. Estratégia de Teste

### 5.1 Técnicas Aplicadas

#### Classes de Equivalência
- **E-mail válido/inválido:** testuser@example.com vs testuser@invalid
- **Username válido/inválido:** username único vs duplicado
- **Senha correta/incorreta:** senha correta vs senha errada

#### Valores Limite
- **Quantidade:** 0, 0.1, 1, N (quantidade máxima)
- **Listas vazias:** 0 alimentos, 0 entradas
- **Calorias restantes:** 0, negativo (deve retornar 0)

#### Tabela de Decisão
- **Estado do usuário × Ação:** Autenticado/Não autenticado × Acessar dashboard
- **Tipo de alimento × Acesso:** Público/Privado × Usuário dono/Outro usuário
- **Quantidade × Validação:** > 0 / <= 0 / vazio

### 5.2 Ciclos de Teste

#### Ciclo 1 - Execução Inicial
- Executar todos os casos de teste (20 casos)
- Registrar defeitos encontrados
- Priorizar correções

#### Ciclo 2 - Regressão
- Reexecutar casos afetados por correções
- Executar caso E2E completo
- Validar bugs corrigidos

### 5.3 Gestão de Defeitos
- **Ferramenta:** GitHub Issues (ou planilha CSV)
- **Campos:** ID, título, descrição, passos, esperado/obtido, severidade, prioridade, status, evidências
- **Severidade:** Alta, Média, Baixa
- **Prioridade:** Alta, Média, Baixa
- **Status:** Aberto, Em Correção, Corrigido, Validado, Fechado

## 6. Papéis e Responsabilidades

- **PO/QA Líder:** Definição de requisitos, aprovação de casos de teste, validação final
- **QA Designer:** Criação de casos de teste, matriz de rastreabilidade
- **Executor:** Execução manual de testes, registro de defeitos, captura de evidências
- **Dev/Automação:** Desenvolvimento de scripts de automação, CI/CD, correção de bugs

## 7. Cronograma

Seguindo o cronograma de 8 semanas do enunciado:

- **Semana 1-2:** Descoberta de requisitos, criação do plano de teste
- **Semana 3-4:** Projeto de casos de teste, matriz de rastreabilidade
- **Semana 5:** Preparação de ambiente, dados de teste
- **Semana 6:** Execução Ciclo 1, registro de defeitos
- **Semana 7:** Correção de bugs, automação mínima, TDD, CI/CD
- **Semana 8:** Ciclo 2 (regressão), métricas, relatório final, apresentação

## 8. Critérios de Entrada

- Ambiente de teste configurado (banco de dados, servidor Flask)
- Dados de teste populados (script seed_data.py executado)
- Casos de teste aprovados e documentados
- Ambiente de automação configurado (Selenium, Postman)

## 9. Critérios de Saída

- ✅ 100% dos casos críticos executados
- ✅ Nenhum bug de severidade Alta aberto
- ✅ Taxa de aprovação ≥ 90% no Ciclo 2
- ✅ Evidências capturadas para todos os casos executados
- ✅ Relatórios gerados (execução, defeitos, métricas, final)

## 10. Ambiente e Ferramentas

### Ambiente
- **Sistema:** Windows 10 / Linux / macOS
- **Python:** 3.11+
- **Framework:** Flask
- **Banco de Dados:** SQLite (calories.db)
- **Servidor:** Local (localhost:5000)

### Ferramentas
- **Testes Unitários/Integração:** pytest, pytest-cov
- **Testes E2E:** Selenium WebDriver, ChromeDriver
- **Testes API:** Postman, Newman
- **CI/CD:** GitHub Actions
- **Gestão de Defeitos:** GitHub Issues
- **Cobertura:** pytest-cov
- **Relatórios:** HTML reports, CSV exports

## 11. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Ambiente instável | Média | Alto | Documentar setup, usar containers |
| Dados inconsistentes | Baixa | Médio | Script de reset entre ciclos |
| Falta de tempo | Média | Alto | Priorizar casos críticos |
| Bugs bloqueadores | Baixa | Alto | Testar cedo, corrigir rápido |
| Evidências perdidas | Baixa | Médio | Organizar por ID, backup |

## 12. Métricas e Relatórios

### Métricas Coletadas
- Taxa de aprovação por ciclo
- Cobertura de requisitos (%)
- Densidade de defeitos (bugs/caso)
- Tempo de correção de bugs
- Cobertura de código (%)

### Relatórios Gerados
- Relatório de Execução (Ciclo 1 e 2)
- Relatório de Defeitos
- Relatório de Métricas
- Relatório Final

