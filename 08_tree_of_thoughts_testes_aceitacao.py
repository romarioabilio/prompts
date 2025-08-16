import os
import re
from groq import Groq

client = Groq(
    api_key="",
)

def call_groq(prompt_text):
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="llama3-70b-8192",
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Erro na chamada da API: {e}")
        return None

def extrair_estrategia_escolhida(texto_avaliacao):
    """Extrai a estratégia escolhida da avaliação do modelo."""
    # Padrões para encontrar a estratégia recomendada
    padroes = [
        r"A estratégia recomendada é (.+?)\.",
        r"A estratégia mais adequada é (.+?)\.",
        r"A estratégia escolhida foi (.+?)\.",
        r"Recomendação:\s*A estratégia (.+?)\.",
        r"Recomendação:\s*(.+?) é a mais adequada",
        r"\*\*Estratégia (.+?)\*\*",
        r"Estratégia (.+?):",
        r"(.+?) é a estratégia recomendada",
        r"(.+?) é a mais adequada",
        r"(.+?) é a estratégia escolhida"
    ]
    
    for padrao in padroes:
        match = re.search(padrao, texto_avaliacao, re.IGNORECASE | re.MULTILINE)
        if match:
            estrategia = match.group(1).strip()
            # Limpar a estratégia de formatação
            estrategia = re.sub(r'\*\*|\*', '', estrategia)  # Remove ** e *
            return estrategia
    
    # Se não encontrou com padrões específicos, procurar por menções de estratégias
    estrategias_conhecidas = [
        "Teste Manual", "Teste Automatizado", "Teste Exploratório", "Teste Baseada em Risco",
        "Manual", "Automatizado", "Exploratório", "Baseada em Risco"
    ]
    
    for estrategia in estrategias_conhecidas:
        if estrategia.lower() in texto_avaliacao.lower():
            return estrategia
    
    return "estratégia mais mencionada" # Fallback caso a extração falhe

def main():
    """
    Tree of Thoughts para Testes de Aceitação
    Avalia diferentes estratégias de teste e escolhe a melhor abordagem.
    """
    problema = "Como testar adequadamente um sistema de pagamento online com múltiplos métodos de pagamento (cartão, PIX, boleto) em um ambiente de produção?"
    print("--- Técnica: Tree of Thoughts para Testes de Aceitação ---")
    print(f"Problema: {problema}\n")

    # --- PASSO 1: GERAR ESTRATÉGIAS DE TESTE ---
    prompt_gerador = f"""
    Para resolver o problema '{problema}', gere 4 estratégias de teste distintas:
    1. Estratégia de Teste Manual
    2. Estratégia de Teste Automatizado
    3. Estratégia de Teste Exploratório
    4. Estratégia de Teste Baseada em Risco
    
    Para cada estratégia, explique:
    - Como seria implementada
    - Vantagens e desvantagens
    - Tempo estimado de execução
    - Cobertura de cenários
    """
    print("--- Passo 1: Gerando estratégias de teste... ---")
    estrategias = call_groq(prompt_gerador)
    if not estrategias: return
    print(f"Estratégias geradas:\n{estrategias}")

    # --- PASSO 2: AVALIAR ESTRATÉGIAS ---
    prompt_avaliador = f"""
    Avaliando as 4 estratégias para o problema '{problema}':
    ---
    Estratégias:
    {estrategias}
    ---
    Avalie cada estratégia em termos de:
    - 'Cobertura de Teste' (1-5)
    - 'Segurança' (1-5) 
    - 'Custo de Implementação' (1-5)
    - 'Tempo de Execução' (1-5)
    - 'Risco de Produção' (1-5)
    
    Ao final, indique claramente qual estratégia deve ser escolhida e por quê.
    """
    print("\n--- Passo 2: Avaliando as estratégias... ---")
    avaliacao = call_groq(prompt_avaliador)
    if not avaliacao: return
    print(f"Avaliação das estratégias:\n{avaliacao}")
    
    # Extrai qual foi a estratégia escolhida pela avaliação
    estrategia_escolhida = extrair_estrategia_escolhida(avaliacao)

    # --- PASSO 3: EXPANSÃO (Detalhar a melhor estratégia) ---
    print("\n--- Passo 3: Detalhamento da Melhor Estratégia ---")
    prompt_expansao = f"""
    Com base na análise anterior, a estratégia escolhida foi: '{estrategia_escolhida}'.

    Agora, crie um plano de implementação detalhado para esta estratégia, incluindo:
    1. Justificativa da escolha
    2. Cronograma de execução
    3. Recursos necessários (pessoas, ferramentas, ambiente)
    4. Cenários de teste específicos
    5. Critérios de sucesso
    6. Plano de contingência
    7. Estratégia de monitoramento durante execução
    """
    print(f"\nDetalhando plano para a estratégia: '{estrategia_escolhida}'...")
    plano_detalhado = call_groq(prompt_expansao)
    if not plano_detalhado: return
    print(f"\n--- Plano de Implementação Final ---\n{plano_detalhado}")

if __name__ == "__main__":
    main() 