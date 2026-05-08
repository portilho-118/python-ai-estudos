# Exercício 37: Utilizando comandos específicos para aperfeiçoar os dados gerados do histórico.

import matplotlib.pyplot as plt

datas = []
tensoes = []

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

            if tipo == "Tensão":
                datas.append(data_hora)
                tensoes.append(valor)

plt.figure(figsize=(10, 5))
plt.plot(datas, tensoes, marker="o", color="royalblue", linewidth=2)

plt.title("Histórico de Tensão")
plt.xlabel("Data e Hora")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.tight_layout()

plt.savefig("grafico_tensao.png")
print(f"Gráfico salvo! {len(tensoes)} Dados plotados com sucesso.")
