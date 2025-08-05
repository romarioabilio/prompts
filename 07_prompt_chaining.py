import os
from groq import Groq


client = Groq(api_key="")

def call_groq(prompt_text):
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="llama3-8b-8192",
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Erro na chamada da API: {e}")
        return None

def main():
    """
    Demonstra Prompt Chaining com um fluxo de desenvolvimento de software.
    """
    print("--- Técnica: Prompt Chaining (Fluxo de Desenvolvimento) ---")
    
    # CADEIA 1: Gerar User Stories
    prompt1 = "Para um novo app de gerenciamento de tarefas, gere 3 'user stories' concisas."
    print(f"\n[Cadeia 1] Enviando prompt: {prompt1}")
    user_stories = call_groq(prompt1)
    if not user_stories: return
    print(f"\n[Cadeia 1] Resposta:\n{user_stories}")

    # CADEIA 2: Detalhar tarefas técnicas
    prompt2 = f"""
    Com base nas user stories a seguir:
    ---
    {user_stories}
    ---
    Escolha a primeira user story e detalhe 3 tarefas técnicas que um desenvolvedor precisaria executar para implementá-la.
    """
    print(f"\n[Cadeia 2] Enviando prompt para detalhar tarefas...")
    tarefas_tecnicas = call_groq(prompt2)
    if not tarefas_tecnicas: return
    print(f"\n[Cadeia 2] Resposta:\n{tarefas_tecnicas}")

    # CADEIA 3: Escrever um exemplo de código
    prompt3 = f"""
    Com base na seguinte lista de tarefas técnicas:
    ---
    {tarefas_tecnicas}
    ---
    Escreva uma função em Python que implemente a primeira tarefa da lista. Inclua comentários no código.
    """
    print(f"\n[Cadeia 3] Enviando prompt para gerar código...")
    codigo_exemplo = call_groq(prompt3)
    if not codigo_exemplo: return
    print(f"\n[Cadeia 3] Resposta Final:\n{codigo_exemplo}")

if __name__ == "__main__":
    main()