# Relatório Final - Projeto Prático de Testes e Qualidade de Software

## Calorie Tracker - Sistema de Rastreamento de Calorias

**Data:** Dezembro 2025  
**Versão do Sistema:** 1.0  
**Equipe:** Grupo de Testes  
**Status:** ✅ Concluído

---

## 1. Resumo Executivo

Este relatório apresenta os resultados finais da execução do projeto prático de Testes e Qualidade de Software para o sistema **Calorie Tracker**, um aplicativo web desenvolvido em Flask para rastreamento de calorias e macronutrientes.

### 1.1 Objetivos Alcançados
- ✅ 100% dos requisitos críticos cobertos por casos de teste
- ✅ 22 casos de teste executados (20 no Ciclo 1 + 2 no Ciclo 2)
- ✅ Taxa de aprovação final: 100% (Ciclo 2)
- ✅ 2 bugs identificados e corrigidos
- ✅ Automação mínima implementada (UI e API)
- ✅ TDD e CI/CD configurados
- ✅ Métricas coletadas e analisadas

---

## 2. Cobertura por Requisito

| Requisito | Descrição | Casos de Teste | Status | Cobertura |
|-----------|-----------|----------------|--------|-----------|
| REQ-001 | Login válido | CT-001 | ✅ | 100% |
| REQ-002 | Login inválido | CT-002 | ✅ | 100% |
| REQ-003 | Registro de usuário | CT-003 | ✅ | 100% |
| REQ-004 | Validação de campos | CT-004, CT-005, CT-006 | ✅ | 100% |
| REQ-005 | Listagem de alimentos | CT-007 | ✅ | 100% |
| REQ-006 | Adicionar entrada válida | CT-008 | ✅ | 100% |
| REQ-007 | Validação de quantidade | CT-009, CT-010, CT-011 | ✅ | 100% |
| REQ-008 | Dashboard - resumo | CT-012 | ✅ | 100% |
| REQ-009 | Cálculo calorias consumidas | CT-013 | ✅ | 100% |
| REQ-010 | Cálculo calorias restantes | CT-014, CT-015 | ✅ | 100% |
| REQ-011 | Acesso alimentos privados | CT-016 | ✅ | 100% |
| REQ-012 | Lista vazia alimentos | CT-017 | ✅ | 100% |
| REQ-013 | Lista vazia entradas | CT-018 | ✅ | 100% |
| REQ-014 | Logout | CT-019 | ✅ | 100% |
| REQ-015 | Proteção de rotas | CT-020 | ✅ | 100% |
| REQ-016 | Fluxo E2E completo | CT-030 | ✅ | 100% |
| REQ-017 | Usabilidade | CT-040 | ✅ | 100% |
| REQ-018 | Performance | CT-041 | ✅ | 100% |

**Total:** 18 requisitos, 22 casos de teste, **100% de cobertura**

---

## 3. Taxa de Aprovação por Ciclo

### Ciclo 1 - Execução Inicial
- **Total de Casos:** 22
- **Passaram:** 20
- **Falharam:** 2
- **Taxa de Aprovação:** 90,9% (20/22)

**Casos que Falharam:**
- CT-030: Fluxo E2E completo (BUG-002)
- CT-040: Usabilidade - mensagens claras (BUG-002)

### Ciclo 2 - Regressão
- **Total de Casos:** 6 (casos afetados + E2E completo)
- **Passaram:** 6
- **Falharam:** 0
- **Taxa de Aprovação:** 100% (6/6)

**Casos Reexecutados:**
- CT-030: ✅ Passou (bug corrigido)
- CT-040: ✅ Passou (bug corrigido)
- CT-001, CT-007, CT-008, CT-012: ✅ Regressão (funcionalidades mantidas)

---

## 4. Densidade de Defeitos

### Métricas Gerais
- **Total de Casos Executados:** 22 casos
- **Total de Bugs Identificados:** 2 bugs
- **Densidade de Defeitos:** 0,09 bugs/caso (baixa)

### Análise por Severidade
- **Alta Severidade:** 1 bug (BUG-001)
- **Média Severidade:** 1 bug (BUG-002)
- **Baixa Severidade:** 0 bugs

### Tempo de Correção
- **BUG-001:** 4 horas
- **BUG-002:** 6 horas
- **Tempo Médio:** 5 horas/bug

---

## 5. Cobertura de Código

### Métricas de Cobertura (pytest-cov)
- **Cobertura Total:** ~85%
- **Models (User, FoodItem, FoodEntry):** 95%
- **Routes (Autenticação):** 90%
- **Routes (API):** 85%
- **Routes (Dashboard):** 80%

### Áreas com Menor Cobertura
- Tratamento de erros específicos (exceções raras)
- Validações de formulários Flask-WTF (alguns casos edge)

---

## 6. Automação

### Testes Automatizados Implementados

#### Testes Unitários (pytest)
- **Total:** 6 testes
- **Cobertura:** Models (User, FoodItem, FoodEntry)
- **Localização:** `tests/unit/test_models.py`
- **Status:** ✅ Todos passando

#### Testes de Integração (pytest + Flask test client)
- **Total:** 4 testes
- **Cobertura:** Rotas de autenticação, APIs REST
- **Localização:** `tests/integration/`
- **Status:** ✅ Todos passando

#### Testes E2E (Selenium WebDriver)
- **Total:** 3 testes
- **Cobertura:** Fluxos completos (registro, login, adicionar entrada)
- **Localização:** `tests/e2e/test_user_journey.py`
- **Status:** ✅ Todos passando

#### Testes API (Postman/Newman)
- **Total:** 5 requisições
- **Cobertura:** APIs REST (GET/POST)
- **Localização:** `automacao/postman/`
- **Status:** ✅ Todos passando

**Total de Testes Automatizados:** 18 testes

---

## 7. TDD e CI/CD

### TDD - Test-Driven Development

**História de Usuário Implementada:**
"Como usuário, quero ver o tempo estimado para atualização do dashboard após adicionar entrada, para entender se preciso aguardar."

**Implementação:**
1. ✅ Teste criado primeiro (falhou)
2. ✅ Código implementado para passar no teste
3. ✅ Refatoração aplicada
4. ✅ Teste passando

**Localização:** `tests/tdd_example/test_tdd_example.py`

### CI/CD - GitHub Actions

**Pipeline Configurado:**
- ✅ Dispara em push/PR
- ✅ Instala dependências (`pip install`)
- ✅ Executa linting
- ✅ Executa testes unitários
- ✅ Executa testes de integração
- ✅ Executa testes E2E (headless)
- ✅ Executa testes Postman (Newman)
- ✅ Gera relatório de cobertura
- ✅ Publica artifacts (relatórios)

**Status:** ✅ Pipeline funcionando corretamente

**Gate:** Falha qualquer teste → PR bloqueado

---

## 8. Riscos Residuais e Recomendações

### Riscos Identificados

1. **Atualização Visual Assíncrona**
   - **Risco:** Dashboard pode não atualizar imediatamente após adicionar entrada
   - **Mitigação:** Implementar polling ou WebSockets para atualização em tempo real
   - **Prioridade:** Média

2. **Testes de Acessibilidade**
   - **Risco:** Sistema pode não estar totalmente acessível (WCAG)
   - **Mitigação:** Implementar testes automatizados com axe-core
   - **Prioridade:** Média

3. **Testes de Performance**
   - **Risco:** Sistema pode ficar lento com muitos dados
   - **Mitigação:** Implementar testes de carga (Locust/JMeter)
   - **Prioridade:** Baixa

4. **Segurança**
   - **Risco:** Falta de testes de segurança (SQL injection, XSS)
   - **Mitigação:** Implementar testes de segurança automatizados
   - **Prioridade:** Média

### Recomendações

1. ✅ **Implementado:** Testes automatizados básicos (UI + API)
2. 🔄 **Em Progresso:** Testes de acessibilidade (recomendado para próxima fase)
3. 🔄 **Futuro:** Testes de performance e carga
4. 🔄 **Futuro:** Testes de segurança automatizados
5. ✅ **Implementado:** CI/CD básico (recomendado expandir)

---

## 9. Lições Aprendidas

### O que Funcionou Bem
- ✅ Estrutura de testes organizada (unit, integration, e2e)
- ✅ Uso de fixtures do pytest para setup/teardown
- ✅ Automação com Selenium para testes E2E
- ✅ Integração com Postman para testes de API
- ✅ CI/CD com GitHub Actions
- ✅ Documentação completa dos casos de teste

### Desafios Enfrentados
- ⚠️ Configuração inicial do ambiente de testes
- ⚠️ Sincronização de dados entre testes
- ⚠️ Captura de evidências (prints/vídeos)
- ⚠️ Tempo limitado para testes manuais completos

### Melhorias para Próximos Projetos
- 📝 Criar templates de casos de teste reutilizáveis
- 📝 Automatizar mais testes manuais
- 📝 Implementar testes de acessibilidade desde o início
- 📝 Criar scripts de geração automática de relatórios

---

## 10. Conclusão

O projeto de Testes e Qualidade de Software para o sistema **Calorie Tracker** foi concluído com sucesso, atingindo todos os objetivos propostos:

- ✅ **100% de cobertura** dos requisitos críticos
- ✅ **100% de taxa de aprovação** no Ciclo 2
- ✅ **2 bugs corrigidos** e validados
- ✅ **Automação mínima** implementada (UI + API)
- ✅ **TDD e CI/CD** configurados e funcionando
- ✅ **Métricas coletadas** e analisadas

O sistema está **estável e pronto para uso**, com todas as funcionalidades críticas testadas e validadas. Os artefatos gerados (plano de teste, casos de teste, matriz de rastreabilidade, relatórios e evidências) estão organizados e disponíveis para referência futura.

---

## 11. Anexos

### Artefatos Entregues
1. ✅ Plano de Teste (`documentos/02_Plano_de_Teste.md`)
2. ✅ Casos de Teste (`planilhas/Casos_de_Teste.csv`)
3. ✅ Matriz de Rastreabilidade (`planilhas/Matriz_Rastreabilidade.csv`)
4. ✅ Scripts de Automação (`automacao/`, `tests/`)
5. ✅ Relatório de Execução (`relatorios/Relatorio_Execucao_Ciclo1.csv`, `Ciclo2.csv`)
6. ✅ Relatório de Defeitos (`relatorios/Relatorio_Defeitos.md`, `.csv`)
7. ✅ Relatório Final (`relatorios/Relatorio_Final.md`)
8. ✅ Evidências (`evidencias/`)

### Estrutura de Evidências
- **Imagens:** IMG-001 a IMG-041 (screenshots dos casos de teste)
- **Vídeos:** VID-001, VID-003, VID-008, VID-030, VID-040 (vídeos dos fluxos principais)

---

**Data de Conclusão:** Dezembro 2025  
**Versão do Relatório:** 1.0  
**Status:** ✅ Aprovado

