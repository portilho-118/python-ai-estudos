# Exercício 38: Utilização de subplots (múltiplos gráficos no mesmo arquivo).

import matplotlib.pyplot as plt

# ---------- Leitura do Histórico ----------

datas_tensao, tensoes = [], []
datas_corrente, correntes = [], []
datas_potencia, potencias = [], []

with open("historico_medicoes.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith("["):
            data_hora = linha[1:17]
            resto = linha[18:]
            partes = resto.split(":")
            if len(partes) < 2:
                continue
            tipo = partes[0].strip()
            valor = float(partes[1].strip().split(" ")[0])

            if tipo == "Tensão":
                datas_tensao.append(data_hora)
                tensoes.append(valor)
            elif tipo == "Corrente":
                datas_corrente.append(data_hora)
                correntes.append(valor)
            elif tipo == "Potência":
                datas_potencia.append(data_hora)
                potencias.append(valor)

# ---------- Subplots ----------

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

ax1.plot(datas_tensao, tensoes, marker="o", color="royalblue", linewidth=2)
ax1.set_title("Tensão (V)")
ax1.set_ylabel("Volts")
ax1.grid(True)

ax2.plot(datas_corrente, correntes, marker="o", color="tomato", linewidth=2)
ax2.set_title("Corrente (A)")
ax2.set_ylabel("Amperes")
ax2.grid(True)

ax3.plot(datas_potencia, potencias, marker="o", color="seagreen", linewidth=2)
ax3.set_title("Potência (W)")
ax3.set_ylabel("Watts")
ax3.grid(True)

plt.tight_layout()
plt.savefig("grafico_subplots.png")
print("Visualização de dados gerada com sucesso!")