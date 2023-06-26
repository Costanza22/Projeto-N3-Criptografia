import sys

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
        print("Uso: python decripta.py <arquivo_chave> <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)
    
    chave_file = sys.argv[1]
    entrada_file = sys.argv[2]
    saida_file = sys.argv[3]
    
    decripta(chave_file, entrada_file, saida_file)
