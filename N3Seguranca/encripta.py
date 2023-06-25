import sys

def encripta(chave_file, entrada_file, saida_file):
    # Lê a chave do arquivo
    with open(chave_file, "r") as chave_arq:
        linhas = chave_arq.readlines()
        modulo = int(linhas[0].strip())
        expoente = int(linhas[1].strip())

    # Lê o dado de entrada do arquivo
    with open(entrada_file, "r") as entrada_arq:
        dado = entrada_arq.read().strip()

    # Codifica o dado como base64
    dado_codificado = dado.encode("utf-8").hex()

    # Divide o dado codificado em chunks
    chunk_size = len(str(modulo))
    chunks = [dado_codificado[i:i+chunk_size] for i in range(0, len(dado_codificado), chunk_size)]

    # Encripta cada chunk usando a chave
    encriptado = [str(pow(int(chunk, 16), expoente, modulo)) for chunk in chunks]

    # Escreve o resultado no arquivo de saída
    with open(saida_file, "w") as saida_arq:
        saida_arq.write("\n".join(encriptado))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python encripta.py <arquivo_chave> <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)
    
    chave_file = sys.argv[1]
    entrada_file = sys.argv[2]
    saida_file = sys.argv[3]
    
    encripta(chave_file, entrada_file, saida_file)
