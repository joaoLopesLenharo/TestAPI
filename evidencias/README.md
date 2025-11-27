# Evidências de Teste

Este diretório contém todas as evidências capturadas durante a execução dos testes do sistema Calorie Tracker.

## Estrutura de Nomenclatura

### Imagens (Screenshots)
- **Formato:** `IMG-XXX.png` ou `IMG-XXX.jpg`
- **Exemplo:** `IMG-001.png` = Screenshot do Caso de Teste CT-001
- **Uso:** Cada evidência deve ter o mesmo número do caso de teste a que se refere

### Vídeos
- **Formato:** `VID-XXX.mp4` ou `VID-XXX.webm`
- **Exemplo:** `VID-001.mp4` = Vídeo da execução do Caso de Teste CT-001
- **Uso:** Vídeos são capturados para casos críticos e fluxos E2E

### Evidências de Falhas
- **Formato:** `IMG-XXX-F.png` ou `VID-XXX-F.mp4`
- **Exemplo:** `IMG-010-F.png` = Screenshot da falha do Caso de Teste CT-010
- **Uso:** Evidências de bugs e falhas identificadas

### Evidências de Regressão
- **Formato:** `IMG-XXX-R.png`
- **Exemplo:** `IMG-001-R.png` = Screenshot da regressão do Caso de Teste CT-001
- **Uso:** Evidências do Ciclo 2 (regressão)

## Lista de Evidências

### Ciclo 1 - Execução Inicial

#### Autenticação
- `IMG-001.png` - CT-001: Login válido (sucesso)
- `VID-001.mp4` - CT-001: Vídeo do fluxo de login
- `IMG-002.png` - CT-002: Login inválido (mensagem de erro)
- `IMG-003.png` - CT-003: Registro de novo usuário
- `VID-003.mp4` - CT-003: Vídeo do fluxo de registro
- `IMG-004.png` - CT-004: Registro com username duplicado
- `IMG-005.png` - CT-005: Registro com email duplicado
- `IMG-006.png` - CT-006: Registro com senhas não coincidem

#### Funcionalidades Principais
- `IMG-007.png` - CT-007: Listagem de alimentos
- `IMG-008.png` - CT-008: Adição de entrada válida
- `VID-008.mp4` - CT-008: Vídeo da adição de entrada
- `IMG-009.png` - CT-009: Validação quantity = 0
- `IMG-010.png` - CT-010: Validação quantity < 0
- `IMG-010-F.png` - CT-010: Bug BUG-001 (quantidade negativa aceita)
- `IMG-011.png` - CT-011: Validação sem food_item_id
- `IMG-012.png` - CT-012: Dashboard com entradas
- `IMG-013.png` - CT-013: Cálculo de calorias consumidas
- `IMG-014.png` - CT-014: Cálculo de calorias restantes
- `IMG-015.png` - CT-015: Calorias restantes nunca negativo

#### Casos Especiais
- `IMG-016.png` - CT-016: Acesso a alimento privado
- `IMG-017.png` - CT-017: Lista vazia de alimentos
- `IMG-018.png` - CT-018: Dashboard com lista vazia
- `IMG-019.png` - CT-019: Logout
- `IMG-020.png` - CT-020: Proteção de rotas

#### E2E e Não Funcional
- `IMG-030.png` - CT-030: Fluxo E2E completo
- `VID-030.mp4` - CT-030: Vídeo do fluxo E2E
- `VID-030-F.mp4` - CT-030: Bug BUG-002 (mensagem truncada)
- `IMG-030-F.png` - CT-030: Screenshot do bug
- `IMG-040.png` - CT-040: Usabilidade - mensagens claras
- `VID-040.mp4` - CT-040: Vídeo de usabilidade
- `IMG-040-F.png` - CT-040: Bug BUG-002 (baixo contraste)
- `IMG-041.png` - CT-041: Performance - tempo de resposta

### Ciclo 2 - Regressão

- `IMG-001-R.png` - CT-001: Regressão login
- `IMG-007-R.png` - CT-007: Regressão listagem
- `IMG-008-R.png` - CT-008: Regressão adição de entrada
- `VID-008-R.mp4` - CT-008: Vídeo de regressão
- `IMG-012-R.png` - CT-012: Regressão dashboard
- `IMG-030.png` - CT-030: E2E após correção (novo)
- `VID-030.mp4` - CT-030: Vídeo após correção
- `IMG-040.png` - CT-040: Usabilidade após correção (novo)
- `VID-040.mp4` - CT-040: Vídeo após correção

## Como Usar

1. **Para Visualizar Evidências:**
   - Abra o arquivo de imagem ou vídeo correspondente ao caso de teste
   - Verifique se a evidência corresponde ao resultado esperado

2. **Para Referenciar em Relatórios:**
   - Use o formato: `IMG-XXX` ou `VID-XXX`
   - Inclua links ou caminhos relativos nos relatórios

3. **Para Adicionar Novas Evidências:**
   - Siga a nomenclatura padrão
   - Use formato PNG para imagens (melhor qualidade)
   - Use formato MP4 para vídeos (compatibilidade)

## Notas

- Todas as evidências foram capturadas no ambiente de teste local
- Screenshots foram tirados em resolução 1920x1080
- Vídeos foram gravados em qualidade HD (720p)
- Evidências de falhas incluem console do navegador quando relevante

