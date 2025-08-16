import os
from groq import Groq

client = Groq(
    api_key="",
)

def main():
    """
    Zero-Shot Prompting para Testes de Aceitação
    Identifica cenários de teste para uma funcionalidade sem exemplos prévios.
    """
    prompt = """
    Como testador de software, identifique os principais cenários de teste de aceitação para a seguinte funcionalidade:

    Funcionalidade: Sistema de Login de Usuário
    - Campo de email
    - Campo de senha
    - Botão "Entrar"
    - Link "Esqueci minha senha"

    Liste os cenários de teste de aceitação que um usuário final executaria para validar se esta funcionalidade está funcionando corretamente.
    Para cada cenário, especifique:
    1. O que o usuário faz
    2. O que deveria acontecer
    3. Critério de aceitação
    """

    print("--- Técnica: Zero-Shot Prompting para Testes de Aceitação ---")
    print(f"Enviando prompt:\n{prompt}")

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Cenários de Teste Identificados ---\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main() 