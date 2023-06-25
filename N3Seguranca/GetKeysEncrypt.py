import sys

def generate_keys():
    modulo = 15212890864824009557
    expoente = 101
    return modulo, expoente


def encripta(chave_file, entrada_file, saida_file):
    # Lê a chave do arquivo
    with open(chave_file, "r") as chave_arq:
        linhas = chave_arq.readlines()
        modulo = int(linhas[0].strip())
        expoente = int(linhas[1].strip())

    # Lê o dado de entrada do arquivo
    with open(entrada_file, "r") as entrada_arq:
        dado = entrada_arq.read().strip()

    # Encripta o dado usando a chave
    encriptado = [str(pow(ord(char), expoente, modulo)) for char in dado]

    # Escreve o resultado no arquivo de saída
    with open(saida_file, "w") as saida_arq:
        saida_arq.write("\n".join(encriptado))


def decripta(chave_file, entrada_file, saida_file):
    # Lê a chave do arquivo
    with open(chave_file, "r") as chave_arq:
        linhas = chave_arq.readlines()
        modulo = int(linhas[0].strip())
        expoente = int(linhas[1].strip())

    # Lê os números encriptados do arquivo de entrada
    with open(entrada_file, "r") as entrada_arq:
        encriptado = [int(line.strip()) for line in entrada_arq.readlines()]

    # Decripta os números usando a chave
    decriptado = [chr(pow(num, expoente, modulo)) for num in encriptado]

    # Escreve o resultado no arquivo de saída
    with open(saida_file, "w") as saida_arq:
        saida_arq.write("".join(decriptado))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python GetKeysEncrypt.py <arquivo_chave> <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    chave_file = sys.argv[1]
    entrada_file = sys.argv[2]
    saida_file = sys.argv[3]

    encripta(chave_file, entrada_file, saida_file)
    decripta(chave_file, saida_file, "decrypted.txt")
