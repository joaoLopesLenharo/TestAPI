# Plano de Teste - Calorie Tracker

**Data:** 2025  
**Versão:** 1.0  
**Grupo:** [Nome do Grupo]

---

## 1. Objetivos do Teste

### Objetivos Gerais
- Verificar se o sistema atende aos requisitos funcionais especificados
- Validar a autenticação e autorização
- Garantir cálculos nutricionais corretos
- Verificar mensagens de erro e sucesso
- Validar limites e validações de dados
- Testar usabilidade básica (clareza de mensagens)
- Validar tempo de resposta básico (<2s em ambiente local)

### Objetivos Específicos
- Testar todos os fluxos de autenticação (login, registro, logout)
- Validar cálculos de calorias e macronutrientes
- Verificar persistência de dados
- Testar validações de formulários
- Validar acesso não autorizado
- Testar fluxo E2E completo

---

## 2. Escopo do Teste

### In Scope (Dentro do Escopo)
- Autenticação (login, registro, logout)
- Gerenciamento de alimentos (listar, adicionar ao diário)
- Cálculos nutricionais (calorias, proteína, carboidratos, gordura)
- Dashboard e visualização de dados
- Validações de formulários
- Mensagens de erro e sucesso
- APIs REST
- Testes de usabilidade básica
- Testes de desempenho básico

### Out of Scope (Fora do Escopo)
- Testes de segurança avançados (penetration testing)
- Testes de carga/stress extensivos
- Testes de acessibilidade completos (WCAG)
- Testes de compatibilidade entre navegadores (apenas Chrome)
- Testes de integração com sistemas externos

---

## 3. Estratégia de Teste

### Níveis de Teste
1. **Testes Unitários:** Modelos, funções de cálculo, validações
2. **Testes de Integração:** Rotas da API, autenticação, banco de dados
3. **Testes de Sistema/E2E:** Fluxos completos do usuário
4. **Testes de Aceitação:** Validação de requisitos do usuário

### Tipos de Teste
1. **Funcionais:**
   - Testes de funcionalidade
   - Testes de regressão
   - Testes de validação
   
2. **Não Funcionais:**
   - Usabilidade básica (clareza de mensagens)
   - Tempo de resposta (<2s)

### Técnicas de Teste
- **Classes de Equivalência:** Login válido/inválido, quantidade válida/inválida
- **Valores Limite:** Quantidade mínima/máxima, lista vazia/cheia
- **Tabela de Decisão:** Estados do sistema × ações do usuário
- **Testes de Fluxo:** Fluxos principais do usuário

### Estratégia de Execução
- **Ciclo 1:** Execução inicial de todos os casos de teste
- **Ciclo 2:** Regressão após correções de bugs
- **Automação:** Mínimo de 3 testes automatizados (login, E2E, API)

---

## 4. Recursos e Papéis

### Papéis do Grupo
- **PO/QA Líder:** Coordenação geral, revisão de requisitos
- **QA Designer:** Criação de casos de teste, matriz de rastreabilidade
- **Executor:** Execução manual de testes, registro de bugs
- **Dev/Automação:** Automação de testes, TDD, CI/CD

### Ferramentas
- **Testes:** pytest, pytest-cov, pytest-html
- **E2E:** Selenium WebDriver
- **API:** Postman/Newman
- **CI/CD:** GitHub Actions
- **Gestão de Bugs:** GitHub Issues
- **Relatórios:** pytest-html, coverage

### Ambiente
- **Desenvolvimento:** Local (Windows/Linux/Mac)
- **Banco de Dados:** SQLite (teste em memória)
- **Navegador:** Chrome (para testes E2E)
- **Python:** 3.11+

---

## 5. Cronograma

### Semana 1-2: Planejamento
- Definição de requisitos testáveis
- Criação do plano de teste
- Início da matriz de rastreabilidade

### Semana 3-4: Preparação
- Elaboração de casos de teste
- Preparação de massa de dados
- Configuração do ambiente

### Semana 5: Execução Manual - Ciclo 1
- Execução de todos os casos de teste
- Registro de bugs
- Geração de relatórios

### Semana 6: Regressão e Automação
- Execução do ciclo 2 (regressão)
- Automação de testes críticos
- Testes de API

### Semana 7: TDD e CI/CD
- Exemplo de TDD
- Configuração de pipeline CI/CD
- Cálculo de métricas

### Semana 8: Finalização
- Relatório final
- Apresentação
- Entrega

---

## 6. Critérios de Entrada e Saída

### Critérios de Entrada
- Ambiente configurado e funcionando
- Massa de dados preparada
- Casos de teste aprovados
- Ferramentas instaladas

### Critérios de Saída
- 100% dos casos críticos executados
- Nenhum bug de severidade Alta aberto
- Cobertura de código ≥ 80%
- Relatórios gerados
- Automação funcionando
- CI/CD configurado

### Critérios de Suspensão
- Ambiente indisponível por mais de 1 dia
- Bugs críticos bloqueando >50% dos testes
- Mudanças significativas nos requisitos

### Critérios de Retomada
- Ambiente restaurado
- Bugs críticos corrigidos
- Requisitos estabilizados

---

## 7. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Ambiente instável | Média | Alto | Backup e documentação |
| Falta de tempo | Média | Alto | Priorização de testes críticos |
| Bugs bloqueadores | Baixa | Alto | Comunicação rápida com dev |
| Mudanças de requisitos | Baixa | Médio | Documentação clara |
| Ferramentas com problemas | Baixa | Médio | Ter alternativas prontas |

---

## 8. Métricas e Relatórios

### Métricas a Coletar
- Cobertura de requisitos (%)
- Taxa de aprovação de testes (%)
- Densidade de defeitos (bugs/caso de teste)
- Tempo de correção de bugs
- Cobertura de código (%)
- Tempo de execução dos testes

### Relatórios a Gerar
- Relatório de execução (ciclo 1 e 2)
- Relatório de defeitos
- Relatório de métricas
- Relatório final

---

## 9. Controle de Configuração

### Versionamento
- Código: Git/GitHub
- Casos de teste: Planilha versionada
- Documentos: Markdown/PDF versionados

### Nomenclatura
- Casos de teste: CT-XXX
- Bugs: BUG-XXX
- Requisitos: REQ-XXX
- Evidências: IMG-XXX, VID-XXX

---

## 10. Aprovações

| Papel | Nome | Data | Assinatura |
|-------|------|------|------------|
| QA Líder | | | |
| PO | | | |

---

**Versão do Documento:** 1.0  
**Última Atualização:** 2025

