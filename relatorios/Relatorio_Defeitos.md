# Relatório de Defeitos - Calorie Tracker

**Data:** 2025  
**Versão:** 1.0

---

## Resumo

- **Total de Defeitos Encontrados:** 2
- **Defeitos Críticos (Alta Severidade):** 0
- **Defeitos de Severidade Média:** 1
- **Defeitos de Severidade Baixa:** 1
- **Defeitos Resolvidos:** 2
- **Defeitos Abertos:** 0

---

## Defeitos Registrados

### BUG-001: Status da entrada não atualiza imediatamente após adição

**Severidade:** Média  
**Prioridade:** Alta  
**Status:** RESOLVIDO  
**Data Abertura:** 2025-01-15  
**Data Fechamento:** 2025-01-20  
**Responsável:** Dev1

**Requisito(s) Afetado(s):** REQ-006  
**Caso(s) de Teste Afetado(s):** CT-007, CT-030

**Descrição:**
Após adicionar um alimento ao diário, o status visual não atualiza imediatamente. É necessário recarregar a página (F5) para ver as mudanças.

**Passos para Reproduzir:**
1. Fazer login no sistema
2. Adicionar um alimento ao diário via API ou interface
3. Observar o dashboard
4. Verificar se os totais foram atualizados

**Resultado Esperado:**
O status e os totais devem atualizar imediatamente após adicionar o alimento, sem necessidade de recarregar a página.

**Resultado Obtido:**
O status só atualiza após recarregar a página manualmente (F5).

**Evidências:**
- IMG-010-F: Screenshot mostrando status desatualizado
- VID-030-F: Vídeo mostrando o problema

**Solução:**
Implementado evento de confirmação do back-end em vez de polling. O front-end agora atualiza automaticamente após receber confirmação do servidor.

**Teste de Regressão:**
CT-007 e CT-030 passaram após a correção.

---

### BUG-002: Mensagem de confirmação truncada no mobile

**Severidade:** Baixa  
**Prioridade:** Média  
**Status:** RESOLVIDO  
**Data Abertura:** 2025-01-15  
**Data Fechamento:** 2025-01-21  
**Responsável:** Dev2

**Requisito(s) Afetado(s):** REQ-014  
**Caso(s) de Teste Afetado(s):** CT-018

**Descrição:**
A mensagem de confirmação ao adicionar alimento fica truncada em dispositivos móveis, dificultando a leitura.

**Passos para Reproduzir:**
1. Acessar o sistema em um dispositivo móvel
2. Fazer login
3. Adicionar um alimento ao diário
4. Observar a mensagem de confirmação

**Resultado Esperado:**
A mensagem deve ser completa e visível, adaptando-se ao tamanho da tela.

**Resultado Obtido:**
A mensagem fica cortada na tela, tornando-se difícil de ler.

**Evidências:**
- VID-030-F: Vídeo mostrando a mensagem truncada

**Solução:**
Ajustado CSS para mensagens responsivas. A mensagem agora se adapta ao tamanho da tela e quebra linha quando necessário.

**Teste de Regressão:**
CT-018 passou após a correção.

---

## Métricas de Defeitos

### Por Severidade

| Severidade | Quantidade | Percentual |
|------------|------------|------------|
| Alta | 0 | 0% |
| Média | 1 | 50% |
| Baixa | 1 | 50% |
| **Total** | **2** | **100%** |

### Por Status

| Status | Quantidade | Percentual |
|--------|------------|------------|
| Resolvido | 2 | 100% |
| Aberto | 0 | 0% |
| **Total** | **2** | **100%** |

### Por Requisito

| Requisito | Defeitos | Status |
|-----------|----------|--------|
| REQ-006 | 1 | Resolvido |
| REQ-014 | 1 | Resolvido |

---

## Análise

### Densidade de Defeitos
- **Total de Casos de Teste:** 20
- **Total de Defeitos:** 2
- **Densidade:** 0.1 defeitos/caso de teste (baixa)

### Tempo de Correção
- **BUG-001:** 5 dias
- **BUG-002:** 6 dias
- **Média:** 5.5 dias

### Riscos Residuais
Nenhum risco residual identificado. Todos os defeitos foram corrigidos e testados.

---

## Recomendações

1. **Testes de Integração:** Adicionar mais testes de integração para cobrir atualizações assíncronas
2. **Testes de Responsividade:** Incluir testes automatizados de responsividade em diferentes tamanhos de tela
3. **Testes de Acessibilidade:** Considerar testes de acessibilidade automatizados (axe)
4. **Testes de Desempenho:** Adicionar testes de desempenho para validar tempo de resposta

---

**Versão do Documento:** 1.0  
**Última Atualização:** 2025-01-22

