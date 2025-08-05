import os
from groq import Groq

client = Groq(
    api_key="",
)

def main():
    """
    Demonstra Chain-of-Thought
    Instrui o modelo a detalhar o raciocínio para um cálculo de armazenamento.
    """
    prompt = """
    Problema: Um desenvolvedor precisa fazer o backup de 3 projetos. O projeto A tem 1.5 GB, o projeto B tem 2048 MB, e o projeto C tem 0.5 GB. 
    Se ele usar um pendrive de 8 GB, quantos megabytes (MB) sobrarão no pendrive?
    
    Pense passo a passo para chegar à resposta final, mostrando as conversões de unidades.
    """

    print("--- Técnica: Chain-of-Thought ---")
    print(f"Enviando prompt:\n{prompt}")

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Resposta do Groq ---\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main()