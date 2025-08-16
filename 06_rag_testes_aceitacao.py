import os
from groq import Groq

client = Groq(
    api_key="",
)

def main():
    """
    RAG para Testes de Aceitação
    Usa documentação de requisitos para gerar cenários de teste específicos.
    """
    pergunta = "Quais cenários de teste de aceitação devo criar para a funcionalidade de cadastro de usuários?"

    # Documentação de requisitos (contexto)
    documentacao_requisitos = """
    Documentação de Requisitos - Sistema de Cadastro de Usuários v1.0
    
    Funcionalidades:
    - Cadastro de usuário com dados pessoais
    - Validação de email único
    - Confirmação de senha
    - Termos de uso obrigatórios
    
    Campos Obrigatórios:
    - Nome completo (mínimo 3 caracteres)
    - Email (formato válido, único no sistema)
    - Senha (mínimo 8 caracteres, 1 maiúscula, 1 número)
    - Confirmação de senha (deve ser igual à senha)
    - Aceite dos termos de uso (checkbox obrigatório)
    
    Regras de Negócio:
    - Email deve ser único no sistema
    - Senha deve ter complexidade mínima
    - Usuário deve aceitar termos para finalizar cadastro
    - Sistema deve enviar email de confirmação após cadastro
    - Usuário deve ativar conta via email antes de fazer login
    
    Validações de Interface:
    - Campos obrigatórios devem ser destacados
    - Mensagens de erro devem ser claras
    - Formulário deve ser responsivo
    - Loading state durante envio
    """

    prompt = f"""
    Use apenas as informações da DOCUMENTAÇÃO abaixo para criar cenários de teste de aceitação específicos.
    Se a informação não estiver na documentação, não inclua no cenário.

    DOCUMENTAÇÃO:
    ---
    {documentacao_requisitos}
    ---
    
    PERGUNTA: {pergunta}
    
    Crie cenários de teste de aceitação que cubram:
    1. Validações de campos obrigatórios
    2. Validações de formato (email, senha)
    3. Regras de negócio (email único, complexidade de senha)
    4. Fluxo de aceite dos termos
    5. Comportamento da interface
    """
    
    print("--- Técnica: RAG para Testes de Aceitação ---")
    print(f"Enviando prompt:\n{prompt}")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Cenários de Teste Baseados na Documentação ---\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main() 