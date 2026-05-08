# Exercício 39: Gráfico de barras para comparação de dados (tipos de medição).

import matplotlib.pyplot as plt

# ---------- Leitura do Histórico ----------

dados = {}

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

            if tipo not in dados:
                dados[tipo] = []
            dados[tipo].append(valor)

# ---------- Calcula a Média por Tipo ----------

tipos = list(dados.keys())
medias = [sum(dados[t]) / len(dados[t]) for t in tipos]

# ---------- Gráfico de Barras ----------

plt.figure(figsize=(10, 6))
plt.bar(tipos, medias, color=["royalblue", "tomato", "seagreen", "orange"])

plt.title("Média por Tipo de Medição")
plt.xlabel("Tipo")
plt.ylabel("Valor Médio")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("grafico_barras.png")
print("Visualização de dados salva com sucesso.")