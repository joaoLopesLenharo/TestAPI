# Estrutura de Apresentação Final
## Calorie Tracker - Projeto Prático de Testes e Qualidade de Software

**Duração:** 10 minutos  
**Formato:** Apresentação oral com slides e demonstração

---

## 1. Introdução e Visão Geral (1 min)

### Slide 1: Título
- **Título:** Calorie Tracker - Projeto Prático de Testes e Qualidade de Software
- **Grupo:** [Nome do Grupo]
- **Data:** 2025

### Slide 2: Visão Geral do Projeto
- **Sistema Testado:** Calorie Tracker
- **Objetivo:** Rastreamento de calorias e macronutrientes
- **Tecnologias:** Flask, Python, SQLite
- **Escopo:** Autenticação, gerenciamento de alimentos, cálculos nutricionais

**Falar:**
- Apresentar o sistema e o objetivo do projeto
- Explicar brevemente o que foi testado

---

## 2. Planejamento e Técnicas (2 min)

### Slide 3: Requisitos e Descoberta
- **15 Requisitos** identificados
- **Formato BDD** (Dado/Quando/Então)
- **Fluxos críticos** mapeados
- **Riscos** identificados

### Slide 4: Plano de Teste
- **Objetivos:** Funcional + Não funcional
- **Níveis:** Unitário, Integração, Sistema/E2E, Aceitação
- **Estratégia:** 2 ciclos (execução + regressão)
- **Técnicas:** Equivalência, Limites, Decisão

### Slide 5: Casos de Teste
- **20 Casos de Teste** criados
- **Técnicas aplicadas:**
  - Classes de Equivalência (login válido/inválido)
  - Valores Limite (quantidade 0/1/N)
  - Tabela de Decisão (estados × ações)
- **1 Caso E2E** completo
- **1 Caso Não Funcional** (usabilidade)

**Falar:**
- Explicar como os requisitos foram transformados em casos de teste
- Mostrar exemplos de técnicas aplicadas
- Destacar a matriz de rastreabilidade

---

## 3. Execução e Evidências (3 min)

### Slide 6: Execução Manual - Ciclo 1
- **20 Casos** executados
- **19 Passaram** (95%)
- **1 Falhou** (CT-030)
- **2 Bugs** identificados

**Demonstração:**
- Mostrar prints/vídeos de evidências
- IMG-001: Login válido
- VID-007: Adição de alimento
- IMG-010-F: Bug identificado

### Slide 7: Defeitos Encontrados
- **BUG-001:** Status não atualiza imediatamente (Média/Alta)
- **BUG-002:** Mensagem truncada no mobile (Baixa/Média)
- **Ambos resolvidos** no ciclo 2

### Slide 8: Execução Manual - Ciclo 2
- **6 Casos** de regressão
- **100% Passaram**
- **Bugs corrigidos** e validados

**Falar:**
- Explicar o processo de execução manual
- Mostrar como os bugs foram registrados
- Destacar a importância da regressão

---

## 4. Automação e CI/CD (2 min)

### Slide 9: Automação de Testes
- **21 Testes Automatizados:**
  - 6 Unitários
  - 8 Integração
  - 3 E2E
  - 4 API (Postman/Newman)

**Demonstração:**
- Executar testes automatizados localmente
- Mostrar relatório de cobertura
- Executar coleção Postman

### Slide 10: TDD - Exemplo
- **História:** Tempo estimado para atualização de status
- **Ciclo Red-Green-Refactor** demonstrado
- **Teste falhando → Código → Refatoração**

**Demonstração:**
- Executar teste TDD
- Mostrar o ciclo completo

### Slide 11: CI/CD Pipeline
- **GitHub Actions** configurado
- **Pipeline automático:**
  - Lint
  - Testes unitários
  - Testes de integração
  - Testes E2E
  - Relatórios de cobertura

**Demonstração:**
- Mostrar pipeline no GitHub Actions
- Mostrar artifacts gerados

**Falar:**
- Explicar a importância da automação
- Mostrar como o CI/CD garante qualidade contínua

---

## 5. Métricas e Lições (2 min)

### Slide 12: Métricas Principais
- **Cobertura de Requisitos:** 100% (15/15)
- **Taxa de Aprovação:** 100% (após correções)
- **Densidade de Defeitos:** 0.1/caso (baixa)
- **Cobertura de Código:** 87% (acima da meta)
- **Tempo de Correção:** 5.5 dias (média)

### Slide 13: Lições Aprendidas
- **Planejamento é Fundamental**
  - Requisitos bem definidos facilitam testes
  - Matriz de rastreabilidade garante cobertura
  
- **Automação Aumenta Confiança**
  - Testes executam mais rápido
  - CI/CD garante qualidade contínua
  
- **TDD Melhora Qualidade**
  - Código testável desde o início
  - Refatoração segura

### Slide 14: Próximos Passos
- Testes de acessibilidade (axe)
- Testes de desempenho
- Monitoramento em produção
- Melhorar cobertura de código

**Falar:**
- Destacar os principais resultados
- Compartilhar lições aprendidas
- Apresentar recomendações

---

## 6. Conclusão (30 seg)

### Slide 15: Conclusão
- ✅ **Objetivos Alcançados**
- ✅ **Qualidade Validada**
- ✅ **Processo Completo**
- ✅ **Pronto para Produção**

**Falar:**
- Resumir os principais pontos
- Agradecer
- Abrir para perguntas

---

## Checklist de Apresentação

### Antes da Apresentação
- [ ] Slides preparados e revisados
- [ ] Evidências organizadas (prints/vídeos)
- [ ] Ambiente de teste configurado
- [ ] Demonstrações testadas
- [ ] Tempo cronometrado (< 10 min)

### Durante a Apresentação
- [ ] Apresentar com clareza
- [ ] Mostrar evidências visuais
- [ ] Executar demonstrações
- [ ] Manter contato visual
- [ ] Responder perguntas

### Materiais Necessários
- [ ] Slides (PowerPoint/PDF)
- [ ] Evidências (prints/vídeos)
- [ ] Ambiente de teste rodando
- [ ] Postman/Newman instalado
- [ ] GitHub Actions acessível

---

## Dicas de Apresentação

1. **Pratique antes:** Ensaiar ajuda a manter o tempo
2. **Seja objetivo:** Focar nos pontos principais
3. **Use evidências:** Mostrar é melhor que apenas falar
4. **Demonstre:** Executar testes ao vivo é impactante
5. **Prepare-se para perguntas:** Antecipe dúvidas comuns

---

**Boa Apresentação! 🎯**

