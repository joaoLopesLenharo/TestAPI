# A) Descoberta e Requisitos Testáveis (1,0)

## Visão & Escopo

**Sistema:** Calorie Tracker - Sistema de Rastreamento de Calorias

**Resumo:** Sistema web desenvolvido em Flask que permite aos usuários registrar-se, fazer login, visualizar alimentos disponíveis, adicionar alimentos ao diário alimentar, acompanhar calorias e macronutrientes consumidos, e visualizar resumo diário com progresso em relação à meta de calorias.

**Fluxos Críticos:**
1. **Autenticação:** Login válido/inválido, registro de novo usuário, logout
2. **Listagem de Alimentos:** Visualizar alimentos públicos e privados do usuário
3. **Adição de Entrada:** Adicionar alimento ao diário com quantidade
4. **Dashboard:** Visualizar resumo diário (calorias, proteínas, carboidratos, gorduras)
5. **Cálculo de Calorias:** Calcular calorias consumidas e restantes
6. **Validações:** Campos obrigatórios, valores inválidos, limites (quantidade > 0)
7. **Mensagens:** Erro/sucesso claras e visíveis

**Riscos Identificados:**
- Autenticação falhar (credenciais inválidas não tratadas adequadamente)
- Inconsistência de dados nutricionais (cálculos incorretos)
- Mensagens pouco claras ou truncadas
- Lentidão ao listar muitos alimentos
- Problemas de acesso a alimentos privados de outros usuários
- Validação insuficiente de campos obrigatórios

## Requisitos com Critérios de Aceitação (BDD)

### REQ-001: Autenticação - Login Válido
**Dado** que sou usuário cadastrado  
**Quando** informo username válido e senha correta  
**Então** devo acessar o sistema e ser redirecionado para o dashboard

### REQ-002: Autenticação - Login Inválido
**Dado** que não sou cadastrado ou a senha está errada  
**Quando** tento fazer login  
**Então** devo ver mensagem "Invalid username or password" e permanecer na página de login

### REQ-003: Registro de Usuário
**Dado** que sou um novo usuário  
**Quando** preencho o formulário de registro com dados válidos e únicos  
**Então** devo ser registrado e redirecionado para a página de login com mensagem de sucesso

### REQ-004: Registro - Validação de Campos
**Dado** que tento me registrar  
**Quando** informo dados inválidos (username duplicado, email inválido, senhas não coincidem)  
**Então** devo ver mensagens de validação apropriadas

### REQ-005: Listagem de Alimentos
**Dado** que há alimentos cadastrados  
**Quando** acesso o dashboard ou a API de alimentos  
**Então** devo ver lista de alimentos públicos e meus alimentos privados com nome, calorias e macronutrientes

### REQ-006: Adicionar Entrada de Alimento
**Dado** que estou autenticado e há alimentos disponíveis  
**Quando** seleciono um alimento e informo quantidade válida (> 0)  
**Então** devo ver a entrada adicionada ao meu diário e o resumo atualizado

### REQ-007: Adicionar Entrada - Validação de Quantidade
**Dado** que tento adicionar uma entrada  
**Quando** informo quantidade <= 0 ou campo vazio  
**Então** devo ver mensagem de erro "Quantity must be greater than 0"

### REQ-008: Dashboard - Visualização de Resumo
**Dado** que tenho entradas no diário  
**Quando** acesso o dashboard  
**Então** devo ver totais de calorias, proteínas, carboidratos e gorduras do dia atual

### REQ-009: Cálculo de Calorias Consumidas
**Dado** que tenho entradas de alimentos no diário  
**Quando** o sistema calcula as calorias do dia  
**Então** devo ver a soma correta de (calorias do alimento × quantidade) para todas as entradas do dia

### REQ-010: Cálculo de Calorias Restantes
**Dado** que tenho uma meta diária de calorias e entradas no diário  
**Quando** o sistema calcula as calorias restantes  
**Então** devo ver (meta diária - calorias consumidas), nunca negativo

### REQ-011: Acesso a Alimentos Privados
**Dado** que outro usuário criou um alimento privado  
**Quando** tento acessar esse alimento via API  
**Então** devo receber erro 403 (Forbidden) ou o alimento não deve aparecer na lista

### REQ-012: Lista Vazia de Alimentos
**Dado** que não há alimentos cadastrados  
**Quando** acesso a lista de alimentos  
**Então** devo ver lista vazia ou mensagem apropriada

### REQ-013: Lista Vazia de Entradas
**Dado** que não tenho entradas no diário de hoje  
**Quando** acesso o dashboard  
**Então** devo ver totais zerados (0 calorias, 0 proteínas, etc.)

### REQ-014: Logout
**Dado** que estou autenticado  
**Quando** clico em logout  
**Então** devo ser desautenticado e redirecionado para a página inicial

### REQ-015: Proteção de Rotas
**Dado** que não estou autenticado  
**Quando** tento acessar dashboard ou APIs protegidas  
**Então** devo ser redirecionado para login ou receber erro 401

### REQ-016: E2E - Fluxo Completo
**Dado** que sou um novo usuário  
**Quando** completo o fluxo: registro → login → visualizar alimentos → adicionar entrada → verificar dashboard  
**Então** todas as etapas devem funcionar corretamente e os dados devem estar consistentes

### REQ-017: Usabilidade - Mensagens Claras
**Dado** que executo qualquer ação no sistema  
**Quando** ocorre sucesso ou erro  
**Então** devo ver mensagens claras, visíveis e compreensíveis em até 3 segundos

### REQ-018: Performance - Tempo de Resposta
**Dado** que acesso qualquer funcionalidade do sistema  
**Quando** faço uma requisição  
**Então** devo receber resposta em menos de 2 segundos (ambiente local)

