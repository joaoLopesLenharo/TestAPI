# Descoberta e Requisitos Testáveis
## Sistema: Calorie Tracker

**Data:** 2025  
**Versão:** 1.0

---

## 1. Visão & Escopo

### Resumo do Sistema
O Calorie Tracker é um sistema web que permite aos usuários:
- Registrar-se e fazer login
- Visualizar alimentos disponíveis
- Adicionar alimentos ao diário alimentar
- Acompanhar calorias e macronutrientes consumidos
- Visualizar resumo diário com progresso em relação à meta de calorias

### Fluxos Críticos
1. **Autenticação:** Login válido/inválido, registro, logout
2. **Gerenciamento de Alimentos:** Listar alimentos, adicionar ao diário
3. **Cálculos Nutricionais:** Calcular totais diários, calorias restantes
4. **Mensagens de Erro/Sucesso:** Feedback claro ao usuário
5. **Limites e Validações:** Campos obrigatórios, valores mínimos/máximos

### Riscos Identificados
- Autenticação falhar permitindo acesso não autorizado
- Inconsistência nos cálculos nutricionais
- Mensagens de erro pouco claras
- Lentidão ao listar muitos alimentos
- Dados não persistidos corretamente

---

## 2. Requisitos com Critérios de Aceitação (BDD)

### REQ-001: Autenticação - Login Válido
**Dado que** sou um usuário cadastrado  
**Quando** informo username válido e senha correta  
**Então** devo acessar o sistema e ser redirecionado para o dashboard  
**E** devo ver meu nome de usuário no topo da página

### REQ-002: Autenticação - Login Inválido
**Dado que** não sou cadastrado ou a senha está errada  
**Quando** tento fazer login  
**Então** devo ver a mensagem "Invalid username or password"  
**E** não devo ser redirecionado para o dashboard

### REQ-003: Registro de Usuário
**Dado que** sou um novo usuário  
**Quando** preencho o formulário de registro com dados válidos (username único, email válido, senhas coincidem)  
**Então** devo ver a mensagem "Congratulations, you are now a registered user!"  
**E** devo ser redirecionado para a página de login

### REQ-004: Registro - Validações
**Dado que** tento me registrar  
**Quando** informo username já existente ou email já cadastrado  
**Então** devo ver mensagem de erro apropriada  
**E** não devo ser registrado

### REQ-005: Listagem de Alimentos
**Dado que** estou autenticado  
**Quando** acesso a lista de alimentos  
**Então** devo ver nome, calorias, proteína, carboidratos e gordura de cada alimento  
**E** devo ver apenas alimentos públicos ou meus próprios alimentos

### REQ-006: Adicionar Alimento ao Diário
**Dado que** estou autenticado e há alimentos disponíveis  
**Quando** seleciono um alimento e informo a quantidade  
**Então** devo ver mensagem de sucesso  
**E** o alimento deve aparecer no meu diário do dia  
**E** os totais nutricionais devem ser atualizados

### REQ-007: Cálculo de Calorias Diárias
**Dado que** estou autenticado e tenho entradas no diário  
**Quando** acesso o dashboard  
**Então** devo ver o total de calorias consumidas hoje  
**E** devo ver as calorias restantes (meta - consumidas)  
**E** devo ver a barra de progresso atualizada

### REQ-008: Cálculo de Macronutrientes
**Dado que** estou autenticado e tenho entradas no diário  
**Quando** acesso o dashboard  
**Então** devo ver totais de proteína, carboidratos e gordura  
**E** os valores devem estar corretos (soma de todas as entradas do dia)

### REQ-009: Lista Vazia de Alimentos
**Dado que** estou autenticado  
**Quando** não há alimentos cadastrados  
**Então** devo ver uma lista vazia ou mensagem apropriada  
**E** não devo ver erros

### REQ-010: Diário Vazio
**Dado que** estou autenticado  
**Quando** não tenho entradas no diário de hoje  
**Então** devo ver totais zerados (0 calorias, 0g proteína, etc.)  
**E** devo ver a meta de calorias completa como restante

### REQ-011: Validação de Quantidade
**Dado que** estou adicionando um alimento ao diário  
**Quando** informo quantidade inválida (negativa, zero, ou não numérica)  
**Então** devo ver mensagem de erro  
**E** o alimento não deve ser adicionado

### REQ-012: Acesso Não Autorizado
**Dado que** não estou autenticado  
**Quando** tento acessar o dashboard ou APIs protegidas  
**Então** devo ser redirecionado para a página de login  
**E** devo ver mensagem apropriada

### REQ-013: Logout
**Dado que** estou autenticado  
**Quando** clico em logout  
**Então** devo ser deslogado  
**E** devo ser redirecionado para a página inicial  
**E** não devo conseguir acessar rotas protegidas

### REQ-014: Usabilidade - Mensagens Claras
**Dado que** estou usando o sistema  
**Quando** realizo qualquer ação  
**Então** as mensagens devem ser claras e visíveis  
**E** os botões devem ter rótulos compreensíveis  
**E** o feedback visual deve aparecer em até 2 segundos

### REQ-015: Desempenho - Tempo de Resposta
**Dado que** estou autenticado  
**Quando** acesso o dashboard ou listo alimentos  
**Então** a página deve carregar em menos de 2 segundos (ambiente local)

---

## 3. Fluxos Principais

### Fluxo 1: Registro e Primeiro Uso
1. Usuário acessa a página inicial
2. Clica em "Register"
3. Preenche formulário de registro
4. É redirecionado para login
5. Faz login
6. Acessa dashboard (vazio)
7. Adiciona primeiro alimento
8. Visualiza resumo atualizado

### Fluxo 2: Uso Diário
1. Usuário faz login
2. Visualiza dashboard com entradas do dia
3. Adiciona novo alimento
4. Verifica totais atualizados
5. Adiciona mais alimentos
6. Verifica progresso em relação à meta
7. Faz logout

### Fluxo 3: Gerenciamento de Alimentos
1. Usuário autenticado acessa lista de alimentos
2. Visualiza alimentos públicos e próprios
3. Adiciona alimento ao diário
4. Verifica entrada no dashboard

---

## 4. Limites e Validações

### Limites de Dados
- **Username:** mínimo 3 caracteres, máximo 80 caracteres, único
- **Email:** formato válido, único
- **Senha:** mínimo 6 caracteres
- **Quantidade:** mínimo 0.1, máximo 1000.0
- **Calorias:** mínimo 0, máximo 10000
- **Meta diária:** mínimo 500, máximo 10000 calorias

### Validações
- Campos obrigatórios: username, email, senha (registro)
- Campos obrigatórios: username, senha (login)
- Quantidade obrigatória ao adicionar alimento
- Validação de tipos de dados (números, strings)

---

## 5. Mensagens de Erro e Sucesso

### Mensagens de Sucesso
- "Congratulations, you are now a registered user!"
- "Alimento adicionado com sucesso" (quando implementado)
- "Entry added" (API)

### Mensagens de Erro
- "Invalid username or password"
- "Please use a different username."
- "Please use a different email address."
- "Passwords must match"
- Erros de validação de campos

---

## 6. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Autenticação falhar | Média | Alto | Testes rigorosos de login/logout |
| Cálculos incorretos | Média | Alto | Testes unitários de cálculos |
| Mensagens pouco claras | Baixa | Médio | Testes de usabilidade |
| Lentidão na listagem | Baixa | Médio | Testes de desempenho |
| Perda de dados | Baixa | Alto | Testes de persistência |

---

## 7. Critérios de Aceitação Gerais

1. Todos os requisitos funcionais devem ser testados
2. Pelo menos 80% de cobertura de código
3. Todos os testes críticos devem passar
4. Tempo de resposta < 2s para operações principais
5. Mensagens claras e visíveis
6. Validações funcionando corretamente
7. Sem bugs críticos (severidade Alta) em produção

