import os
from groq import Groq

client = Groq(
    api_key="",
)

def main():
    """
    Chain-of-Thought para Testes de Aceitação
    Raciocina passo a passo sobre cenários de teste complexos.
    """
    prompt = """
    Problema de Teste: Um sistema de e-commerce precisa validar se um pedido pode ser finalizado.
    
    Regras de negócio:
    - Cliente deve estar logado
    - Carrinho deve ter pelo menos 1 item
    - Estoque deve ser suficiente para todos os itens
    - Endereço de entrega deve estar completo
    - Forma de pagamento deve ser válida
    - Valor total deve ser maior que R$ 10,00
    
    Cenário: Cliente logado, carrinho com 2 produtos (R$ 25,00 cada), estoque OK, endereço completo, cartão válido, mas valor total é R$ 50,00.
    
    Pense passo a passo:
    1. Quais regras de negócio se aplicam a este cenário?
    2. Quais validações devem ser executadas?
    3. Qual seria o resultado esperado do teste?
    4. Que dados de teste seriam necessários para validar completamente este cenário?
    
    Apresente sua análise detalhada.
    """

    print("--- Técnica: Chain-of-Thought para Testes de Aceitação ---")
    print(f"Enviando prompt:\n{prompt}")

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Análise Detalhada do Cenário de Teste ---\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main() 