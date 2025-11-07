# Testes de API com Postman/Newman

Este diretório contém a coleção Postman para testes de API do Calorie Tracker.

## Pré-requisitos

- Postman instalado (opcional, para uso via GUI)
- Newman instalado (para execução via linha de comando)

## Instalação do Newman

```bash
npm install -g newman
```

## Executando os Testes

### Via Postman GUI

1. Abra o Postman
2. Importe a coleção: `CalorieTracker.postman_collection.json`
3. Importe o ambiente: `local.postman_environment.json`
4. Execute a coleção

### Via Newman (Linha de Comando)

```bash
# Executar coleção com ambiente local
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json

# Executar com relatório HTML
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json -r html

# Executar com relatório JSON
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json -r json

# Executar com relatório CLI detalhado
newman run CalorieTracker.postman_collection.json -e local.postman_environment.json --verbose
```

## Estrutura da Coleção

- **Autenticação:**
  - Login Válido
  - Login Inválido

- **Alimentos:**
  - Listar Alimentos (GET)
  - Listar Alimentos - Não Autorizado

- **Entradas:**
  - Adicionar Entrada (POST)
  - Adicionar Entrada - Quantidade Inválida

## Notas

- Certifique-se de que o servidor está rodando em `http://localhost:5000` antes de executar os testes
- Para testes que requerem autenticação, você precisa fazer login primeiro ou usar cookies de sessão

