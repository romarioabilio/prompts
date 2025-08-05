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

def extrair_plano_escolhido(texto_avaliacao):
    """Extrai o plano escolhido da avaliação do modelo."""
    match = re.search(r"A abordagem a ser tentada primeiro é a (.+?)\.", texto_avaliacao, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "primeira abordagem mencionada" # Fallback caso a extração falhe

def main():
    """
    Demonstra o conceito de Tree of Thoughts (ToT) .
    Ciclo: Gerar pensamentos -> Avaliar pensamentos -> Expandir o melhor pensamento.
    """
    problema = "Como otimizar uma query `SELECT * FROM pedidos WHERE status = 'processando'` que está lenta em uma tabela com 20 milhões de linhas?"
    print("--- Técnica: Tree of Thoughts (Otimização de Query SQL) ---")
    print(f"Problema: {problema}\n")

    # --- PASSO 1: GERAR PENSAMENTOS (Gerar abordagens de otimização) ---
    prompt_gerador = f"Para resolver o problema '{problema}', gere 3 abordagens de otimização distintas e explique o porquê de cada uma."
    print("--- Passo 1: Gerando abordagens de otimização... ---")
    pensamentos = call_groq(prompt_gerador)
    if not pensamentos: return
    print(f"Abordagens geradas:\n{pensamentos}")

    # --- PASSO 2: AVALIAR PENSAMENTOS (O modelo avalia os próprios caminhos) ---
    prompt_avaliador = f"""
    Avaliando as 3 abordagens para o problema '{problema}':
    ---
    Abordagens:
    {pensamentos}
    ---
    Avalie cada abordagem em termos de 'Impacto na Performance' e 'Complexidade de Implementação' (de 1 a 5). 
    Ao final, indique claramente qual abordagem deve ser tentada primeiro e por quê.
    """
    print("\n--- Passo 2: Avaliando as abordagens... ---")
    avaliacao = call_groq(prompt_avaliador)
    if not avaliacao: return
    print(f"Avaliação das abordagens:\n{avaliacao}")
    
    # Extrai qual foi o plano escolhido pela avaliação
    plano_escolhido = extrair_plano_escolhido(avaliacao)

    # --- PASSO 3: EXPANSÃO (Detalhar o melhor pensamento) ---
    print("\n--- Passo 3: Expansão do Melhor Pensamento ---")
    prompt_expansao = f"""
    Com base na análise anterior, a abordagem escolhida foi: '{plano_escolhido}'.

    Agora, crie um plano de ação detalhado para implementar esta abordagem.
    Inclua os seguintes pontos:
    1. A justificativa resumida da escolha.
    2. O comando SQL exato para implementar a solução (por exemplo, `CREATE INDEX ...`).
    3. O comando SQL para verificar se a otimização funcionou (por exemplo, `EXPLAIN ANALYZE ...`).
    """
    print(f"\nGerando plano de ação para a abordagem: '{plano_escolhido}'...")
    plano_final = call_groq(prompt_expansao)
    if not plano_final: return
    print(f"\n--- Plano de Ação Final ---\n{plano_final}")


if __name__ == "__main__":
    main()