# Exemplo de TDD (Test-Driven Development)

Este diretório contém um exemplo prático de TDD seguindo o ciclo Red-Green-Refactor.

## História de Usuário

**Como usuário, quero ver o tempo estimado para atualização do status após adicionar alimento, para entender se preciso aguardar.**

## Ciclo TDD

### 1. Red (Vermelho) - Teste Falha

Primeiro, escrevemos o teste que inicialmente falha:

```python
def test_status_update_eta_local():
    environment = 'local'
    max_expected_time = 2.0
    eta = get_status_update_eta(environment)
    assert eta <= max_expected_time  # FALHA: retorna 5.0
```

**Executar:** `pytest tests/tdd_example/test_tdd_example.py::test_status_update_eta_local -v`

**Resultado:** ❌ FALHA (esperado)

### 2. Green (Verde) - Teste Passa

Agora, implementamos o código mínimo para fazer o teste passar:

```python
def get_status_update_eta(environment='local'):
    if environment == 'local':
        return 2.0  # Ajustado para passar no teste
    return 10.0
```

**Executar:** `pytest tests/tdd_example/test_tdd_example.py::test_status_update_eta_local -v`

**Resultado:** ✅ PASSA

### 3. Refactor (Refatoração)

Refatoramos o código para melhorar a qualidade sem quebrar os testes:

```python
def get_status_update_eta(environment='local'):
    """
    Retorna o tempo estimado baseado em eventos assíncronos do back-end.
    Em vez de polling, usa evento de confirmação.
    """
    # Configurações por ambiente
    config = {
        'local': 2.0,      # Evento assíncrono local
        'production': 5.0  # Evento assíncrono produção
    }
    
    return config.get(environment, 5.0)
```

**Executar:** `pytest tests/tdd_example/test_tdd_example.py -v`

**Resultado:** ✅ Todos os testes passam

## Executando os Testes

```bash
# Executar todos os testes TDD
pytest tests/tdd_example/ -v

# Executar teste específico
pytest tests/tdd_example/test_tdd_example.py::test_status_update_eta_local -v

# Executar com output detalhado
pytest tests/tdd_example/ -v -s
```

## Lições Aprendidas

1. **Red:** Escreva o teste primeiro, mesmo que falhe
2. **Green:** Implemente o código mínimo para passar
3. **Refactor:** Melhore o código sem quebrar os testes
4. **Repita:** Continue o ciclo para novas funcionalidades

## Próximos Passos

- Integrar com eventos reais do back-end
- Adicionar tratamento de erros (timeout)
- Adicionar testes de integração
- Medir tempo real de atualização

