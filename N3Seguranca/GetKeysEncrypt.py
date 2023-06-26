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

    encriptado = [str(pow(ord(char), expoente, modulo)) for char in dado]

    with open(saida_file, "w") as saida_arq:
        saida_arq.write("\n".join(encriptado))


def decripta(chave_file, entrada_file, saida_file):
    with open(chave_file, "r") as chave_arq:
        linhas = chave_arq.readlines()
        modulo = int(linhas[0].strip())
        expoente = int(linhas[1].strip())

    with open(entrada_file, "r") as entrada_arq:
        encriptado = [int(line.strip()) for line in entrada_arq.readlines()]

    decriptado = [chr(pow(num, expoente, modulo)) for num in encriptado]

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
