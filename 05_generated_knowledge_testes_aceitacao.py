import os
from groq import Groq

client = Groq(
    api_key="",
)

def main():
    """
    Generated Knowledge para Testes de Aceitação
    Gera conhecimento sobre padrões de teste e depois aplica esse conhecimento.
    """
    pergunta_principal = "Como criar cenários de teste de aceitação para um sistema de pagamento online?"

    # PASSO 1: Gerar conhecimento sobre padrões de teste
    prompt_gerador_conhecimento = """
    Gere 5 padrões fundamentais de teste de aceitação para sistemas de pagamento online, incluindo:
    - Tipos de validações necessárias
    - Cenários de erro comuns
    - Regras de negócio críticas
    - Considerações de segurança
    - Fluxos de usuário típicos
    """
    
    print("--- Técnica: Generated Knowledge para Testes de Aceitação (Passo 1: Gerando Conhecimento) ---")
    print(f"Enviando prompt gerador de conhecimento:\n{prompt_gerador_conhecimento}")

    try:
        completion_conhecimento = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_gerador_conhecimento}],
            model="llama3-8b-8192",
        )
        conhecimento_gerado = completion_conhecimento.choices[0].message.content
        print("\n--- Conhecimento Gerado sobre Padrões de Teste ---\n")
        print(conhecimento_gerado)

    except Exception as e:
        print(f"\nOcorreu um erro ao gerar conhecimento: {e}")
        return
 
    # PASSO 2: Aplicar o conhecimento gerado
    prompt_final = f"""
    Com base nos seguintes padrões de teste identificados:
    
    Padrões:
    {conhecimento_gerado}

    Agora, crie cenários de teste de aceitação específicos para um sistema de pagamento online que inclui:
    - Cartão de crédito/débito
    - PIX
    - Boleto bancário
    
    Para cada método de pagamento, crie 2 cenários de teste de aceitação seguindo os padrões identificados.
    """

    print("\n\n--- Técnica: Generated Knowledge (Passo 2: Aplicando Conhecimento) ---")
    print(f"Enviando prompt para criar cenários específicos...")
    
    try:
        completion_final = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_final}],
            model="llama3-8b-8192",
        )
        resposta_final = completion_final.choices[0].message.content
        print("\n--- Cenários de Teste de Aceitação Gerados ---\n")
        print(resposta_final)

    except Exception as e:
        print(f"\nOcorreu um erro ao gerar cenários: {e}")

if __name__ == "__main__":
    main() 