# J) Apresentação Final (0,1)

## Estrutura da Apresentação (10 minutos)

### 1. SUT & Escopo (1 min)

**O que apresentar:**
- Sistema: **Calorie Tracker** - Rastreamento de Calorias
- Tecnologia: Flask (Python), SQLite, HTML/CSS/JS
- Funcionalidades principais:
  - Autenticação (login/registro)
  - Listagem de alimentos
  - Adição de entradas ao diário
  - Dashboard com resumo nutricional
- Escopo de testes: 18 requisitos, 22 casos de teste

**Slide/Demo:**
- Mostrar o sistema rodando (dashboard)
- Explicar brevemente o que o sistema faz

---

### 2. Plano & Técnicas (2 min)

**O que apresentar:**
- Níveis de teste: Unitário, Integração, Sistema/E2E, Aceitação
- Tipos: Funcional + Não funcional (usabilidade, performance)
- Técnicas aplicadas:
  - **Classes de Equivalência:** Login válido/inválido, email válido/inválido
  - **Valores Limite:** Quantidade (0, 0.1, 1, N), listas vazias
  - **Tabela de Decisão:** Estado do usuário × Ação, Tipo de alimento × Acesso
- Estratégia: 2 ciclos (execução inicial + regressão)

**Slide/Demo:**
- Mostrar matriz de rastreabilidade (planilha)
- Explicar como as técnicas foram aplicadas nos casos

---

### 3. Casos e Evidências (3 min)

**O que apresentar:**
- 22 casos de teste criados
- Exemplos de casos críticos:
  - CT-001: Login válido ✅
  - CT-002: Login inválido ✅
  - CT-008: Adicionar entrada válida ✅
  - CT-010: Validação de quantidade (BUG-001 encontrado)
  - CT-030: Fluxo E2E completo (BUG-002 encontrado)
- Evidências capturadas: 43 evidências (screenshots + vídeos)

**Slide/Demo:**
- Mostrar alguns prints/vídeos rápidos:
  - `IMG-001.png` - Login válido
  - `VID-008.mp4` - Adição de entrada
  - `IMG-010-F.png` - Bug encontrado
  - `VID-030.mp4` - Fluxo E2E após correção
- Explicar como os bugs foram identificados e corrigidos

---

### 4. Automação & CI (2 min)

**O que apresentar:**
- **Testes Automatizados:**
  - Unitários: 6 testes (pytest)
  - Integração: 4 testes (Flask test client)
  - E2E: 3 testes (Selenium)
  - API: 5 requisições (Postman/Newman)
- **Total:** 18 testes automatizados (81,8% dos casos)
- **CI/CD:** GitHub Actions configurado
  - Pipeline executa todos os testes
  - Gera relatórios de cobertura
  - Bloqueia PRs se testes falharem

**Slide/Demo:**
- Mostrar execução dos testes rodando:
  ```bash
  pytest tests/ --cov=app
  ```
- Mostrar print do GitHub Actions (se disponível)
- Mostrar relatório de cobertura HTML

---

### 5. Métricas & Lições (2 min)

**O que apresentar:**

**Métricas:**
- Cobertura de requisitos: **100%** (18/18)
- Taxa de aprovação Ciclo 1: **90,9%** (20/22)
- Taxa de aprovação Ciclo 2: **100%** (6/6)
- Densidade de defeitos: **0,09 bugs/caso** (baixa)
- Cobertura de código: **~85%**
- Bugs identificados: **2** (ambos corrigidos)

**Lições Aprendidas:**
- ✅ Estrutura organizada facilitou execução
- ✅ Automação economizou tempo
- ⚠️ Testes manuais ainda necessários para usabilidade
- 📝 Documentação completa é essencial

**Próximos Passos:**
- Expandir testes de acessibilidade
- Implementar testes de performance
- Aumentar cobertura para 90%+

**Slide/Demo:**
- Mostrar gráfico/tabela de métricas
- Mostrar relatório final (PDF ou HTML)

---

## Dicas para Apresentação

### Preparação
1. **Teste tudo antes:** Certifique-se de que o sistema está rodando
2. **Prepare evidências:** Tenha prints/vídeos prontos para mostrar
3. **Pratique o timing:** 10 minutos é pouco, seja objetivo
4. **Prepare backup:** Tenha slides ou PDF caso a demo falhe

### Durante a Apresentação
1. **Seja objetivo:** Foque nos pontos principais
2. **Mostre evidências:** Prints/vídeos são mais impactantes que slides
3. **Demonstre conhecimento:** Explique as técnicas aplicadas
4. **Mostre resultados:** Métricas e bugs encontrados

### Divisão de Tempo Sugerida
- **Pessoa 1:** SUT & Escopo (1 min) + Plano & Técnicas (2 min)
- **Pessoa 2:** Casos e Evidências (3 min)
- **Pessoa 3:** Automação & CI (2 min) + Métricas & Lições (2 min)

---

## Checklist de Apresentação

### Antes da Apresentação
- [ ] Sistema rodando e testado
- [ ] Evidências organizadas e acessíveis
- [ ] Slides/PDF preparados (opcional)
- [ ] Scripts de teste funcionando
- [ ] Relatórios gerados
- [ ] Equipe alinhada sobre quem fala o quê

### Durante a Apresentação
- [ ] Apresentar SUT de forma clara
- [ ] Explicar técnicas aplicadas
- [ ] Mostrar evidências (prints/vídeos)
- [ ] Demonstrar automação rodando
- [ ] Apresentar métricas e resultados
- [ ] Responder perguntas do professor

### Após a Apresentação
- [ ] Disponibilizar artefatos (se solicitado)
- [ ] Responder dúvidas adicionais
- [ ] Coletar feedback

---

## Estrutura de Slides (Opcional)

Se optar por usar slides, sugestão de estrutura:

1. **Slide 1:** Título - Calorie Tracker - Testes e Qualidade
2. **Slide 2:** SUT & Escopo (visão geral)
3. **Slide 3:** Plano de Teste (níveis, tipos, técnicas)
4. **Slide 4:** Casos de Teste (exemplos + evidências)
5. **Slide 5:** Automação (testes automatizados + CI/CD)
6. **Slide 6:** Métricas (gráficos/tabelas)
7. **Slide 7:** Lições Aprendidas & Próximos Passos
8. **Slide 8:** Obrigado / Perguntas

---

## Organização dos Artefatos para Entrega

### Estrutura Final

```
Trabalho testes de software/
├── documentos/
│   ├── 01_Descoberta_Requisitos_Testaveis.md
│   ├── 02_Plano_de_Teste.md
│   ├── 03_Dados_Ambiente.md
│   └── 04_Guia_Apresentacao.md
├── planilhas/
│   ├── Casos_de_Teste.csv
│   └── Matriz_Rastreabilidade.csv
├── automacao/
│   ├── postman/
│   │   ├── CalorieTracker.postman_collection.json
│   │   └── local.postman_environment.json
│   └── README.md
├── relatorios/
│   ├── Relatorio_Execucao_Ciclo1.csv
│   ├── Relatorio_Execucao_Ciclo2.csv
│   ├── Relatorio_Defeitos.csv
│   ├── Relatorio_Defeitos.md
│   ├── Relatorio_Metricas.csv
│   └── Relatorio_Final.md
├── evidencias/
│   └── README.md (estrutura documentada)
├── tests/ (scripts de automação)
├── scripts/
│   └── seed_data.py
└── README.md
```

### Formato de Entrega

1. **Plano de Teste:** `documentos/02_Plano_de_Teste.md` (ou converter para PDF/DOCX)
2. **Casos de Teste + Matriz:** `planilhas/Casos_de_Teste.csv` e `planilhas/Matriz_Rastreabilidade.csv` (ou converter para XLSX)
3. **Scripts de Automação:** `automacao/` e `tests/` (com README)
4. **Relatórios:** `relatorios/` (execução, defeitos, métricas, final)
5. **Evidências:** `evidencias/` (estrutura documentada no README)

---

**Boa sorte na apresentação! 🚀**

