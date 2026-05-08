# Exercício 35: como utilizar o pandas para normalizar os dados e exportar a tabela para Microsoft Excel. 

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

df = pd.DataFrame(registros)
df.to_excel("historico_medicoes.xlsx", index=False)
print("Arquivo do Microsoft Excel gerado com sucesso!")