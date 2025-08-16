# Técnicas de Prompting para Testes de Aceitação

Este projeto demonstra como adaptar diferentes técnicas de prompting de IA para o contexto de **testes de aceitação em engenharia de software**.

## 📋 Técnicas Implementadas

### 1. **Zero-Shot Prompting** (`01_zero_shot_testes_aceitacao.py`)
- **Objetivo**: Identificar cenários de teste sem exemplos prévios
- **Aplicação**: Análise inicial de funcionalidades para identificar casos de teste críticos
- **Exemplo**: Identificar cenários de teste para sistema de login

### 2. **Few-Shot Prompting** (`02_few_shot_testes_aceitacao.py`)
- **Objetivo**: Classificar tipos de bugs com base em exemplos
- **Aplicação**: Categorização automática de defeitos encontrados durante testes
- **Exemplo**: Classificar bugs como funcional, usabilidade, performance, etc.

### 3. **Chain-of-Thought** (`03_chain_of_thought_testes_aceitacao.py`)
- **Objetivo**: Raciocinar passo a passo sobre cenários complexos
- **Aplicação**: Análise detalhada de regras de negócio e validações
- **Exemplo**: Validar fluxo completo de finalização de pedido

### 4. **Self-Consistency** (`04_self_consistency_testes_aceitacao.py`)
- **Objetivo**: Validar consistência na identificação de cenários
- **Aplicação**: Executar múltiplas vezes para encontrar cenários mais robustos
- **Exemplo**: Identificar cenários críticos de cadastro de produtos

### 5. **Generated Knowledge** (`05_generated_knowledge_testes_aceitacao.py`)
- **Objetivo**: Gerar conhecimento sobre padrões de teste e aplicá-lo
- **Aplicação**: Criar frameworks de teste baseados em padrões conhecidos
- **Exemplo**: Gerar padrões para testes de pagamento online

### 6. **RAG (Retrieval-Augmented Generation)** (`06_rag_testes_aceitacao.py`)
- **Objetivo**: Usar documentação para gerar cenários específicos
- **Aplicação**: Criar testes baseados em requisitos documentados
- **Exemplo**: Gerar cenários de teste para cadastro de usuários

### 7. **Prompt Chaining** (`07_prompt_chaining_testes_aceitacao.py`)
- **Objetivo**: Criar fluxo completo de planejamento de testes
- **Aplicação**: Automatizar processo de criação de planos de teste
- **Exemplo**: Identificar funcionalidades → Criar cenários → Gerar dados → Criar plano

### 8. **Tree of Thoughts** (`08_tree_of_thoughts_testes_aceitacao.py`)
- **Objetivo**: Avaliar diferentes estratégias e escolher a melhor
- **Aplicação**: Decidir entre abordagens de teste (manual, automatizado, exploratório)
- **Exemplo**: Escolher estratégia para testar sistema de pagamento

## 🚀 Como Usar

### Pré-requisitos
```bash
pip install groq
```

### Configuração
1. Configure sua API key do Groq em cada arquivo
2. Escolha a técnica apropriada para seu cenário

### Exemplos de Uso

#### Para Identificar Cenários Iniciais:
```bash
python 01_zero_shot_testes_aceitacao.py
```

#### Para Classificar Bugs:
```bash
python 02_few_shot_testes_aceitacao.py
```

#### Para Análise Complexa:
```bash
python 03_chain_of_thought_testes_aceitacao.py
```

## 📊 Casos de Uso Práticos

### 1. **Planejamento de Testes**
- Use **Zero-Shot** para identificar cenários iniciais
- Use **RAG** para basear testes em documentação
- Use **Prompt Chaining** para criar plano completo

### 2. **Execução de Testes**
- Use **Chain-of-Thought** para analisar cenários complexos
- Use **Self-Consistency** para validar cenários críticos
- Use **Generated Knowledge** para aplicar padrões conhecidos

### 3. **Análise de Resultados**
- Use **Few-Shot** para classificar bugs encontrados
- Use **Tree of Thoughts** para escolher estratégias de correção

### 4. **Melhoria Contínua**
- Use **Generated Knowledge** para criar frameworks reutilizáveis
- Use **RAG** para manter testes alinhados com documentação

## 🎯 Vantagens das Adaptações

### Para Testadores:
- **Automação**: Reduz trabalho manual de criação de cenários
- **Consistência**: Padroniza abordagens de teste
- **Cobertura**: Identifica cenários que poderiam ser esquecidos
- **Documentação**: Mantém testes alinhados com requisitos

### Para Equipes:
- **Colaboração**: Facilita comunicação entre testadores e desenvolvedores
- **Qualidade**: Melhora cobertura e qualidade dos testes
- **Eficiência**: Acelera processo de criação de testes
- **Manutenção**: Facilita atualização de testes quando requisitos mudam

## 🔧 Personalização

Cada técnica pode ser personalizada para:
- **Domínio específico** (e-commerce, saúde, financeiro)
- **Tipo de aplicação** (web, mobile, desktop)
- **Metodologia** (ágil, waterfall, DevOps)
- **Ferramentas** (Selenium, Cypress, Playwright)

## 📈 Próximos Passos

1. **Integração com Ferramentas**: Conectar com ferramentas de teste existentes
2. **Automação Completa**: Criar pipelines de teste automatizados
3. **Métricas**: Implementar medição de efetividade das técnicas
4. **Expansão**: Adicionar mais técnicas específicas para QA

---

**Desenvolvido para TCC - Pesquisa em Engenharia de Software**
*Adaptação de técnicas de prompting para contexto de testes de aceitação* 