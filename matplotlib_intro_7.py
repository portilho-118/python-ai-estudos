# Exercício 42: Utilizando cores adicionais para alerta visual por faixa de tensão.

import matplotlib.pyplot as plt

# ---------- Leitura do Histórico ----------

datas = []
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
                datas.append(linha[1:17])
                tensoes.append(valor)

# ---------- Definição das Cores das Faixas ----------

TENSAO_MIN = 100
TENSAO_MAX = 250

cores = []
for t in tensoes:
    if t < TENSAO_MIN:
        cores.append("red")
    elif t > TENSAO_MAX:
        cores.append("orange")
    else:
        cores.append("green")

# ---------- Gráfico ----------

plt.figure(figsize=(10, 6))
plt.plot(datas, tensoes, color="royalblue", linewidth=2)
plt.scatter(datas, tensoes, color=cores, s=100, zorder=5)

plt.axhline(y=TENSAO_MIN, color="red", linestyle="--", linewidth=1, label="Mínimo (100V)")
plt.axhline(y=TENSAO_MAX, color="orange", linestyle="--", linewidth=1, label="Máximo (250V)")

plt.title("Monitoramento de Tensão - Alerta por Faixa")
plt.xlabel("Data e Hora")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("grafico_alertas.png")
print("Visualização de dados salvo com sucesso!")