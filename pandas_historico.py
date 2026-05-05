# Exercício 32: utilização da função with open para leitura de dados de um arquivo

"""

Observações:
1. Utiliza-se with open ("nome do arquivo", "r") as "nome da chave": para poder realizar a leitura do arquivo .txt;
2. for linha in arquivo: executa um loop para guardar os valores em linhas = []
3. linhas.append(linha.strip()) acrescenta uma linha a cada leitura;
4. for linha in linhas realiza o loop para ler cada linha criada pelo sistema.
    print(linha)

"""

import pandas as pd

registros = []
with open("historico_medicoes.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()   # linha.strip() retira – no início e fim – os espaços e quebras de linha do código (\n)
        if linha.startswith("["):   # linha.startswith() possui a função de filtrar os resultados que possuem "[]" no código.
            registros.append(linha)

for r in registros:
    print(r)