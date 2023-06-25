# Projeto-N3-Criptografia


Dupla: Giovana.C e Costanza


No código fornecido anteriormente, foi utilizado Python como linguagem de programação. A escolha do Python foi feita devido à sua simplicidade, clareza e ampla disponibilidade de bibliotecas para manipulação de números grandes e criptografia.Estavamos na dúvida sobre utilizar Java como segunda linguagem mas Python era o que mais dominavamos.

O código foi organizado em funções para facilitar a legibilidade e reutilização. A função `ler_arquivo` é responsável por ler um arquivo e retornar uma lista de inteiros longos. A parte principal do código lê os arquivos de chaves e o arquivo criptografado, descriptografa o texto criptografado e converte os inteiros longos de volta para o texto plano. Em seguida, o texto descriptografado é escrito em um arquivo de saída.

Durante o desenvolvimento do código, foram encontrados alguns problemas, como erros de leitura e conversão de inteiros longos. Esses problemas foram resolvidos fazendo uso correto das funções e bibliotecas apropriadas como o gmpy2 ou bigInt

Para testar o código, utilizamos casos de teste que incluiam diferentes chaves públicas e textos criptografados. Verificando se o texto descriptografado corresponde ao texto original e se o arquivo de saída é gerado corretamente, nesse caso os números 3 e 5 foram utilizados mas como teste outros números inteiros primos poderiam ter sido utilizados nesse projeto.

Outras Bibliotecas parecidas:

1. Cryptography: Uma biblioteca de alto nível, ela suporta vários algoritmos criptográficos, incluindo RSA, AES, DES, entre outros.

2. PyCryptodome: Uma biblioteca que oferece uma ampla gama de algoritmos criptográficos, incluindo RSA, AES, DES, entre outros. É uma versão atualizada e mantida da antiga biblioteca PyCrypto.

3. pyOpenSSL: Uma biblioteca que fornece uma interface Python para as funções da biblioteca OpenSSL. Ela oferece suporte a várias operações criptográficas, como criptografia simétrica e assimétrica,

No geral, o projeto pode ser uma ótima oportunidade para aprender sobre criptografia, programação e manipulação de dados.
