import os
from groq import Groq


client = Groq(
    api_key="",
)

def main():
    """
    Demonstra Generated Knowledge
    Gera fatos sobre Docker e VMs para depois compará-los.
    """
    pergunta_principal = "Qual a diferença fundamental entre um contêiner Docker e uma Máquina Virtual (VM)?"

    # PASSO 1: Gerar fatos
    prompt_gerador_fatos = "Gere 4 fatos técnicos e concisos sobre o funcionamento de contêineres Docker e de Máquinas Virtuais."
    print("--- Técnica: Generated Knowledge (Passo 1: Gerando Fatos) ---")
    print(f"Enviando prompt gerador de fatos:\n{prompt_gerador_fatos}")

    try:
        completion_fatos = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_gerador_fatos}],
            model="llama3-8b-8192",
        )
        fatos_gerados = completion_fatos.choices[0].message.content
        print("\n--- Fatos Gerados pelo Groq ---\n")
        print(fatos_gerados)

    except Exception as e:
        print(f"\nOcorreu um erro ao gerar fatos: {e}")
        return

    # PASSO 2: Usar os fatos gerados
    prompt_final = f"""
    Com base nos seguintes fatos:
    
    Fatos:
    {fatos_gerados}

    Responda à seguinte pergunta de forma clara para um desenvolvedor júnior: "{pergunta_principal}"
    """

    print("\n\n--- Técnica: Generated Knowledge (Passo 2: Respondendo com Fatos) ---")
    print(f"Enviando prompt final...")
    
    try:
        completion_final = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_final}],
            model="llama3-8b-8192",
        )
        resposta_final = completion_final.choices[0].message.content
        print("\n--- Resposta Final do Groq ---\n")
        print(resposta_final)

    except Exception as e:
        print(f"\nOcorreu um erro ao gerar resposta final: {e}")

if __name__ == "__main__":
    main()