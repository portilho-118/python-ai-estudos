# Exercício 40: utilização de histograma para visualização de dados com a ferramenta Matplotlib.

import matplotlib.pyplot as plt

# ---------- Leitura do Histórico ----------

tensoes = []

with open("historico_medicoes.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith("["):
            resto = linha[18:]
            partes = resto.split(":")
            if len(partes) < 2:
                continue
            tipo = partes[0].strip()
            valor = float(partes[1].strip().split(" ")[0])

            if tipo == "Tensão":
                tensoes.append(valor)

# ---------- Histograma ----------

plt.figure(figsize=(10, 6))
plt.hist(tensoes, bins=5, color="royalblue", edgecolor="black")

plt.title("Distribuição dos Valores de Tensão")
plt.xlabel("Tensão (V)")
plt.ylabel("Frequência")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("grafico_histograma.png")
print(f"Visualização de dados salva com sucesso! Foram realizadas {len(tensoes)} no total." )