import os
from groq import Groq

client = Groq(
    api_key="",
)
 
def main():
    """
    Few-Shot Prompting para Testes de Aceitação
    Classifica tipos de bugs com base em exemplos de cenários de teste.
    """
    prompt = """
    Classifique o tipo de bug encontrado no cenário de teste a seguir com uma das categorias: 'funcional', 'usabilidade', 'performance', 'segurança', 'compatibilidade', 'interface', 'dados'.

    Cenário: "Usuário tenta fazer login com email válido e senha correta, mas o sistema retorna erro 500"
    Tipo: funcional

    Cenário: "Botão de 'Salvar' está muito pequeno e difícil de clicar em dispositivos móveis"
    Tipo: usabilidade

    Cenário: "Página de listagem de produtos demora mais de 10 segundos para carregar"
    Tipo: performance

    Cenário: "Sistema aceita senha com apenas 3 caracteres"
    Tipo: segurança

    Cenário: "Formulário não funciona corretamente no navegador Safari"
    Tipo: compatibilidade

    Cenário: "Campo de data permite inserir texto ao invés de apenas números"
    Tipo: interface

    Cenário: "Dados do usuário são perdidos após atualizar a página"
    Tipo: dados

    Cenário: "Sistema permite login com credenciais de usuário deletado"
    Tipo:
    """

    print("--- Técnica: Few-Shot Prompting para Testes de Aceitação ---")
    print(f"Enviando prompt:\n{prompt}")

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Classificação do Bug ---\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main() 