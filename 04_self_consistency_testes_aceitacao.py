import os
from groq import Groq
from collections import Counter

client = Groq(
    api_key="",
)

def extrair_cenarios_finais(texto):
    """Extrai os cenários de teste identificados do texto de resposta."""
    cenarios = []
    linhas = texto.splitlines()
    
    for linha in linhas:
        linha_upper = linha.upper()
        # Capturar diferentes formatos de cenários
        marcadores = [
            "CENÁRIO:", "CENARIO:", "CENÁRIO 1:", "CENARIO 1:",
            "CENÁRIO 2:", "CENARIO 2:", "CENÁRIO 3:", "CENARIO 3:",
            "**CENÁRIO", "**CENARIO", "CENÁRIO", "CENARIO"
        ]
        
        for marcador in marcadores:
            if marcador in linha_upper:
                # Extrair texto após o marcador
                if ":" in linha:
                    parte_cenario = linha.split(":", 1)[1].strip()
                else:
                    # Para casos sem ":", pegar o resto da linha
                    parte_cenario = linha.replace(marcador, "").strip()
                
                if parte_cenario and len(parte_cenario) > 5:  # Evitar strings muito pequenas
                    cenarios.append(parte_cenario)
                break
    
    # Se não encontrou cenários com marcadores, tentar extrair por contexto
    if not cenarios:
        for i, linha in enumerate(linhas):
            if "cenário" in linha.lower() or "cenario" in linha.lower():
                # Pegar a próxima linha como possível cenário
                if i + 1 < len(linhas):
                    proxima_linha = linhas[i + 1].strip()
                    if proxima_linha and len(proxima_linha) > 10:
                        cenarios.append(proxima_linha)
    
    return cenarios
 
def main():
    """
    Self-Consistency para Testes de Aceitação
    Executa múltiplas vezes para validar consistência na identificação de cenários de teste.
    """
    prompt = """
    Como testador de software, identifique os 3 cenários de teste de aceitação mais críticos para a seguinte funcionalidade:

    Funcionalidade: Sistema de Cadastro de Produtos
    - Campo "Nome do Produto" (obrigatório)
    - Campo "Preço" (obrigatório, numérico)
    - Campo "Categoria" (dropdown com opções)
    - Campo "Descrição" (opcional, texto longo)
    - Botão "Salvar"
    - Botão "Cancelar"

    Para cada cenário crítico, use o formato:
    CENÁRIO: [descrição do cenário]

    Foque nos cenários que validam regras de negócio críticas e validações obrigatórias.
    """

    print("--- Técnica: Self-Consistency para Testes de Aceitação ---")
    print(f"Enviando prompt:\n{prompt}")

    num_tentativas = 3
    todos_cenarios = []

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
            
            cenarios = extrair_cenarios_finais(resposta_completa)
            if cenarios:
                todos_cenarios.extend(cenarios)
            else:
                print(f"AVISO: Não foi possível extrair cenários na tentativa {i+1}.")

        except Exception as e:
            print(f"\nOcorreu um erro na tentativa {i+1}: {e}")

    if not todos_cenarios:
        print("Não foi possível extrair cenários de teste.")
        return

    # Análise de consistência
    contagem = Counter(todos_cenarios)
    cenarios_mais_frequentes = contagem.most_common(3)

    print("\n--- Análise de Consistência dos Cenários ---")
    print(f"Total de cenários identificados: {len(todos_cenarios)}")
    print(f"Cenários únicos: {len(set(todos_cenarios))}")
    print("\nCenários mais consistentes (identificados em múltiplas tentativas):")
    
    for cenario, frequencia in cenarios_mais_frequentes:
        print(f"- {cenario} (identificado {frequencia} vezes)")

if __name__ == "__main__":
    main() 