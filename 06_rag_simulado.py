import os
from groq import Groq


client = Groq(
    api_key="",
)

def main():
    """
    Demonstra uma simulação de RAG
    Responde uma pergunta com base em um trecho de documentação de API.
    """
    pergunta = "Qual o endpoint para deletar um usuário pelo ID e qual método HTTP devo usar?"

   
    contexto_recuperado = """
    Documentação da API de Usuários v2.1
    
    Recursos:
    - GET /api/users: Lista todos os usuários.
    - GET /api/users/{id}: Busca um usuário específico pelo ID.
    - POST /api/users: Cria um novo usuário. Campos obrigatórios: 'nome', 'email'.
    - PUT /api/users/{id}: Atualiza todos os dados de um usuário.
    - DELETE /api/users/{id}: Deleta o usuário especificado. Requer autenticação de admin.
    """

    prompt = f"""
    Use apenas as informações do CONTEXTO abaixo para responder à PERGUNTA.
    Se a resposta não estiver no contexto, diga "Não encontrei essa informação na documentação".

    CONTEXTO:
    ---
    {contexto_recuperado}
    ---
    
    PERGUNTA: {pergunta}
    """
    
    print("--- Técnica: RAG ) ---")
    print(f"Enviando prompt:\n{prompt}")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        resposta = chat_completion.choices[0].message.content
        print("\n--- Resposta do Groq --- (baseada apenas no contexto)\n")
        print(resposta)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main()