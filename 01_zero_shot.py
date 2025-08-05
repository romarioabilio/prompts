import os
from groq import Groq


client = Groq(
    api_key="",
)

def main():
    """
    Zero-Shot Prompting
    Pede ao modelo para identificar a linguagem de um trecho de código.
    """
    prompt = """
    Identifique a linguagem de programação do código abaixo e descreva brevemente sua finalidade.

    Código:
    ```
    function calcularTotal(itens) {
      let total = 0;
      for (const item of itens) {
        total += item.preco * item.quantidade;
      }
      return total;
    }
    ```
    
    Linguagem e Finalidade:
    """

    print("--- Técnica: Zero-Shot Prompting ---")
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