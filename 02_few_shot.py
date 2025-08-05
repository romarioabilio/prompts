import os
from groq import Groq


client = Groq(
    api_key="",
)

def main():
    """
    Few-Shot Prompting
    Classifica o tipo de uma mensagem de commit com base em exemplos.
    """
    prompt = """
    Classifique a mensagem de commit a seguir com um dos tipos: 'feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore'.

    Mensagem: "docs: atualiza o guia de instalação no README.md"
    Tipo: docs

    Mensagem: "feat: adiciona login com conta do Google"
    Tipo: feat

    Mensagem: "fix: corrige erro que impedia o usuário de salvar o perfil"
    Tipo: fix

    Mensagem: "refactor: melhora performance da função de busca de produtos"
    Tipo: refactor

    Mensagem: "style: aplica formatação do linter nos arquivos do projeto"
    Tipo:
    """

    print("--- Técnica: Few-Shot Prompting ---")
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