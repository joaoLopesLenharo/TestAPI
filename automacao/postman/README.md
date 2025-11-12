# Testes de API com Postman/Newman

Este diretório contém a coleção Postman completa para testes de API do Calorie Tracker com autenticação automática.

## 📋 Pré-requisitos

- **Postman** instalado (opcional, para uso via GUI)
- **Newman** instalado (para execução via linha de comando)
- **Node.js** instalado (necessário para instalar o Newman)
- **Servidor Flask** rodando em `http://localhost:5000`

## 🔧 Instalação

### Instalar Node.js

Baixe e instale o Node.js de: https://nodejs.org/

### Instalar Newman

```bash
npm install -g newman
```

### Instalar Reporter HTML (Opcional)

```bash
npm install -g newman-reporter-html
```

## 🚀 Executando os Testes

### Opção 1: Script Python (Recomendado)

```bash
# Execute o script que faz tudo automaticamente
python automacao/postman/run_postman_tests.py
```

O script:
- Verifica se o Newman está instalado
- Verifica se o servidor está rodando
- Executa os testes
- Gera relatórios HTML e JSON

### Opção 2: Via Postman GUI

1. Abra o Postman
2. Importe a coleção: `CalorieTracker.postman_collection.json`
3. Importe o ambiente: `local.postman_environment.json`
4. Selecione o ambiente "Local"
5. Execute a coleção completa ou testes individuais

### Opção 3: Via Newman (Linha de Comando)

```bash
# Navegue até o diretório do projeto
cd "F:\codes\python\Trabalho testes de software"

# Executar coleção com ambiente local
newman run automacao/postman/CalorieTracker.postman_collection.json \
  -e automacao/postman/local.postman_environment.json

# Executar com relatório HTML
newman run automacao/postman/CalorieTracker.postman_collection.json \
  -e automacao/postman/local.postman_environment.json \
  -r html \
  --reporter-html-export automacao/postman/reports/report.html

# Executar com relatório JSON
newman run automacao/postman/CalorieTracker.postman_collection.json \
  -e automacao/postman/local.postman_environment.json \
  -r json \
  --reporter-json-export automacao/postman/reports/report.json

# Executar com relatório CLI detalhado
newman run automacao/postman/CalorieTracker.postman_collection.json \
  -e automacao/postman/local.postman_environment.json \
  --verbose
```

## 📁 Estrutura da Coleção

### Setup - Autenticação
- **1. Login Válido**: Testa login com credenciais válidas e salva cookie de sessão
- **2. Login Inválido**: Testa login com credenciais inválidas

### API - Alimentos
- **1. Listar Alimentos (Autenticado)**: Lista todos os alimentos (requer autenticação)
- **2. Listar Alimentos - Não Autorizado**: Testa acesso sem autenticação (deve retornar 401)
- **3. Criar Alimento (POST)**: Cria um novo alimento

### API - Entradas
- **1. Adicionar Entrada (POST)**: Adiciona uma entrada de comida
- **2. Adicionar Entrada - Quantidade Inválida**: Testa validação com quantidade negativa
- **3. Adicionar Entrada - Alimento Inexistente**: Testa erro com alimento que não existe
- **4. Listar Entradas (GET)**: Lista todas as entradas do usuário

## 🔐 Autenticação Automática

A coleção foi configurada para:
- Fazer login automaticamente quando necessário
- Salvar o cookie de sessão em variáveis de ambiente
- Reutilizar a sessão em testes subsequentes
- Limpar cookies quando necessário para testes de não autorização

## 📊 Variáveis de Ambiente

O arquivo `local.postman_environment.json` contém:

- `base_url`: URL base da API (http://localhost:5000)
- `test_username`: Usuário de teste (testuser)
- `test_password`: Senha de teste (test123)
- `session_cookie`: Cookie de sessão (gerado automaticamente)
- `food_item_id`: ID do alimento (gerado automaticamente)
- `created_food_id`: ID do alimento criado (gerado automaticamente)
- `created_entry_id`: ID da entrada criada (gerado automaticamente)

## 📈 Relatórios

Os relatórios são gerados em `automacao/postman/reports/`:

- **HTML**: Relatório visual completo com estatísticas
- **JSON**: Dados estruturados para análise programática
- **CLI**: Saída no terminal durante a execução

## ✅ Validações dos Testes

Cada teste inclui validações para:
- Status codes HTTP corretos
- Estrutura de resposta JSON
- Campos obrigatórios presentes
- Mensagens de erro apropriadas
- Cookies de sessão quando necessário

## 🐛 Solução de Problemas

### Erro: "Newman não encontrado"
- Instale o Node.js: https://nodejs.org/
- Instale o Newman: `npm install -g newman`

### Erro: "Servidor não está rodando"
- Inicie o servidor Flask: `python app.py`
- Verifique se está rodando em `http://localhost:5000`

### Erro: "401 Unauthorized"
- Verifique se o usuário de teste existe no banco de dados
- Execute o script de seed: `python scripts/seed_data.py`
- Verifique as credenciais no ambiente do Postman

### Testes falhando
- Verifique se o servidor está rodando
- Verifique se o banco de dados tem dados de teste
- Execute os testes na ordem correta (a coleção está organizada)

## 📝 Notas

- Os testes são executados na ordem definida na coleção
- A autenticação é feita automaticamente quando necessário
- Variáveis são compartilhadas entre testes na mesma execução
- Relatórios são gerados automaticamente com timestamp

