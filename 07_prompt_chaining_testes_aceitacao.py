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
    Prompt Chaining para Testes de Aceitação
    Cria um fluxo completo de planejamento de testes.
    """
    print("--- Técnica: Prompt Chaining para Testes de Aceitação ---")
    
    # CADEIA 1: Identificar funcionalidades críticas
    prompt1 = """
    Para um sistema de e-commerce, identifique as 3 funcionalidades mais críticas que precisam de testes de aceitação prioritários.
    Considere o impacto no negócio e a frequência de uso pelos usuários.
    """
    print(f"\n[Cadeia 1] Identificando funcionalidades críticas...")
    funcionalidades_criticas = call_groq(prompt1)
    if not funcionalidades_criticas: return
    print(f"\n[Cadeia 1] Funcionalidades críticas:\n{funcionalidades_criticas}")

    # CADEIA 2: Criar cenários de teste para a primeira funcionalidade
    prompt2 = f"""
    Com base nas funcionalidades críticas identificadas:
    ---
    {funcionalidades_criticas}
    ---
    Escolha a primeira funcionalidade e crie 5 cenários de teste de aceitação detalhados.
    Para cada cenário, especifique:
    - Pré-condições
    - Passos de execução
    - Resultado esperado
    - Critério de aceitação
    """
    print(f"\n[Cadeia 2] Criando cenários de teste...")
    cenarios_teste = call_groq(prompt2)
    if not cenarios_teste: return
    print(f"\n[Cadeia 2] Cenários de teste:\n{cenarios_teste}")

    # CADEIA 3: Gerar dados de teste
    prompt3 = f"""
    Com base nos cenários de teste criados:
    ---
    {cenarios_teste}
    ---
    Gere dados de teste específicos para cada cenário, incluindo:
    - Dados válidos para cenários positivos
    - Dados inválidos para cenários negativos
    - Dados boundary para testes de limite
    - Dados extremos para testes de stress
    """
    print(f"\n[Cadeia 3] Gerando dados de teste...")
    dados_teste = call_groq(prompt3)
    if not dados_teste: return
    print(f"\n[Cadeia 3] Dados de teste:\n{dados_teste}")

    # CADEIA 4: Criar plano de execução
    prompt4 = f"""
    Com base nos cenários e dados de teste:
    ---
    Cenários: {cenarios_teste}
    Dados: {dados_teste}
    ---
    Crie um plano de execução de testes de aceitação que inclua:
    - Ordem de execução dos cenários
    - Estimativa de tempo por cenário
    - Dependências entre cenários
    - Critérios de aprovação/reprovação
    - Estratégia de reporte de bugs
    """
    print(f"\n[Cadeia 4] Criando plano de execução...")
    plano_execucao = call_groq(prompt4)
    if not plano_execucao: return
    print(f"\n[Cadeia 4] Plano de execução final:\n{plano_execucao}")

if __name__ == "__main__":
    main() 