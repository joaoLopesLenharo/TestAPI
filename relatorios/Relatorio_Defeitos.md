# Relatório de Defeitos

## Resumo Executivo

Durante a execução dos testes do sistema Calorie Tracker, foram identificados **2 defeitos**, todos corrigidos e validados no Ciclo 2 de testes.

- **Total de Bugs:** 2
- **Bugs Críticos (Alta Severidade):** 1
- **Bugs Corrigidos:** 2
- **Taxa de Correção:** 100%

---

## BUG-001: Validação de quantidade não bloqueia valores negativos

### Informações Gerais
- **ID:** BUG-001
- **Requisito Afetado:** REQ-007
- **Caso de Teste:** CT-010
- **Severidade:** Alta
- **Prioridade:** Alta
- **Status:** CORRIGIDO ✅
- **Data Abertura:** 2025-11-27
- **Data Fechamento:** 2025-11-28
- **Tempo de Correção:** 4 horas

### Descrição
A API `/api/entry` aceita valores negativos para o campo `quantity` sem validação adequada, permitindo criar entradas com quantidades inválidas, o que pode causar inconsistências nos cálculos nutricionais.

### Passos para Reproduzir
1. Fazer login no sistema
2. Enviar requisição POST para `/api/entry` com:
   ```json
   {
     "food_item_id": 1,
     "quantity": -1
   }
   ```

### Resultado Esperado
- Status HTTP 400 (Bad Request)
- Mensagem de erro: "Quantity must be greater than 0"

### Resultado Obtido
- Status HTTP 201 (Created)
- Entrada criada com quantidade negativa
- Cálculos nutricionais incorretos

### Ambiente
- Navegador: Chrome 126
- Framework: Flask (ambiente local)
- Python: 3.11

### Evidência
- **IMG-010-F:** Screenshot da requisição bem-sucedida com quantidade negativa

### Correção Aplicada
Validação adicionada no endpoint `/api/entry`:
```python
if quantity <= 0:
    return jsonify({'error': 'Quantity must be greater than 0'}), 400
```

### Validação
✅ Teste CT-010 reexecutado e passou após correção

---

## BUG-002: Mensagem de confirmação truncada e contraste baixo em mobile

### Informações Gerais
- **ID:** BUG-002
- **Requisito Afetado:** REQ-017
- **Casos de Teste:** CT-030, CT-040
- **Severidade:** Média
- **Prioridade:** Média
- **Status:** CORRIGIDO ✅
- **Data Abertura:** 2025-11-27
- **Data Fechamento:** 2025-12-01
- **Tempo de Correção:** 6 horas

### Descrição
Em dispositivos móveis, a mensagem de confirmação de sucesso ao adicionar entrada é truncada (cortada), dificultando a leitura. Além disso, o botão "Adicionar Alimento" possui contraste insuficiente, dificultando a visualização.

### Passos para Reproduzir
1. Acessar o sistema em dispositivo mobile ou modo responsivo do navegador
2. Fazer login
3. Adicionar uma entrada de alimento
4. Verificar a mensagem de confirmação e o botão "Adicionar Alimento"

### Resultado Esperado
- Mensagem de confirmação completa e visível
- Botão com contraste adequado (WCAG AA mínimo)

### Resultado Obtido
- Mensagem cortada na tela mobile
- Botão com contraste insuficiente (difícil visualização)

### Ambiente
- Navegador: Mobile Chrome
- Resolução: 375x667 (iPhone SE)
- Framework: Flask (ambiente local)

### Evidência
- **VID-030-F:** Vídeo mostrando mensagem truncada
- **IMG-040-F:** Screenshot do botão com baixo contraste

### Correção Aplicada
1. Ajuste de CSS para mensagens responsivas (word-wrap, max-width)
2. Aumento do contraste do botão (de #4CAF50 para #2E7D32 com texto branco)

### Validação
✅ Testes CT-030 e CT-040 reexecutados e passaram após correção

---

## Métricas de Defeitos

### Por Severidade
- **Alta:** 1 bug (50%)
- **Média:** 1 bug (50%)
- **Baixa:** 0 bugs (0%)

### Por Status
- **Corrigidos:** 2 bugs (100%)
- **Em Correção:** 0 bugs (0%)
- **Abertos:** 0 bugs (0%)

### Tempo Médio de Correção
- **BUG-001:** 4 horas
- **BUG-002:** 6 horas
- **Média:** 5 horas

### Densidade de Defeitos
- **Total de Casos Executados:** 22 casos
- **Total de Bugs:** 2 bugs
- **Densidade:** 0,09 bugs/caso (baixa)

---

## Conclusão

Todos os defeitos identificados foram corrigidos e validados. O sistema está estável e pronto para uso, com todas as funcionalidades críticas funcionando corretamente.

