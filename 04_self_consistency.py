import os
from groq import Groq
from collections import Counter


client = Groq(
    api_key="",
)


def extrair_resposta_final(texto):
    for linha in texto.splitlines():
        if "RESPOSTA_FINAL:" in linha:
            parte_numerica = linha.split("RESPOSTA_FINAL:")[1].strip()
            return parte_numerica
    return None 

def main():
    """
    Demonstra Self-Consistency
    Executa um cálculo de transferência de dados várias vezes para encontrar a resposta mais comum.
    """
    prompt = """
    Problema: Um data center tem um link de 1 Gbps (gigabit por segundo). Quanto tempo, em segundos, levaria para transferir um arquivo de 750 MB (megabytes)?
    
    Pense passo a passo. Lembre-se que 1 gigabit = 1000 megabits, e 1 megabyte = 8 megabits.
    
    Ao final do seu raciocínio, apresente o resultado numérico em uma linha separada no seguinte formato:
    RESPOSTA_FINAL: [número de segundos]
    """
    
    print("--- Técnica: Self-Consistency ---")
    print(f"Enviando prompt:\n{prompt}")
    
    num_tentativas = 3
    respostas = []

    print(f"\nExecutando o prompt {num_tentativas} vezes...\n")

    for i in range(num_tentativas):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
                temperature=0.7,
            )
            resposta_completa = chat_completion.choices[0].message.content
            print(f"--- Resposta da Tentativa {i+1} ---\n{resposta_completa}\n")
            
            resposta_final = extrair_resposta_final(resposta_completa)
            if resposta_final:
                respostas.append(resposta_final)
            else:
                print(f"AVISO: Não foi possível encontrar a tag RESPOSTA_FINAL: na tentativa {i+1}.")


        except Exception as e:
            print(f"\nOcorreu um erro na tentativa {i+1}: {e}")

    if not respostas:
        print("Não foi possível extrair respostas finais.")
        return

    contagem = Counter(respostas)
    resposta_consistente = contagem.most_common(1)[0][0]

    print("\n--- Análise de Consistência ---")
    print(f"Respostas finais extraídas: {respostas}")
    print(f"A resposta final mais consistente é: {resposta_consistente} segundos")

if __name__ == "__main__":
    main()