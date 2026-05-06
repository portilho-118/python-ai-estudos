# Exercício 34: continuação no uso do DataFrame para organização de informações utilizando descibe, max e filtros.

"""
Observações:
1. data_hora = linha[1:16] possui a função de acessar os valores entre 1 e 15 (exatamente os valores da data e hora);
2. resto = linha[18:] acessa o restante das informações;
3. Lembre-se que este acesso é realizado de forma diferente... Se opondo a listas (lista = ["..."]), neste caso os objetos são
strings. Chamamos este processo de slicing.
4. Divide a string pelo ":", ou seja, cada tipo de dado é separado:
    a. partes[0]: o tipo;
    b. partes[1]: valor e unidade juntos;
    c. partes[1].strip().split(): remove os espaços e os dividem.
5. Cuidado ao misturar unidades diferentes em uma mesma análise estatística,
essa mistura pode apresentar valores que não condizem com os dados esperados para o estudo.
"""

import pandas as pd

registros = []
with open("historico_medicoes.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith("["):
            data_hora = linha[1:17]

            resto = linha[18:]

            partes = resto.split(":")
            tipo = partes[0].strip()
            valor_unidade = partes[1].strip().split(" ")
            valor = float(valor_unidade[0])
            unidade = valor_unidade[1]

            registros.append({

                "data_hora": data_hora,
                "tipo": tipo,
                "valor": valor,
                "unidade": unidade

            })

            print(f"Total de registros, {len(registros)}")
            df = pd.DataFrame(registros)
            print(df)

            print(df["valor"].describe())   # opter as estatísticas dos valores;

            tensoes = df[df["tipo"] == "Tensão"]    # sistema de filtro para as medições de tensão;
            print(tensoes)

            print(f"Maior medição: {df['valor'].max()}")   # obtenção do valor máximo medido;

            tensoes = df[df["tipo"] == "Tensão"]
            print("\n=== Estatísticas de Tensão ===")
            print(tensoes["valor"].describe().round(2))