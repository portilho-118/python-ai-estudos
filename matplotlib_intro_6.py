# Exercício 41: realizando anotações no gráfico (máximo e mínimo).

"""
Observação:
1. tensoes.index(valor_max) busca o valor dentro da lista e retorna a posição onde ele está;
    a. valor_max = max(tensoes) aponta o valor de interesse;
    b. idx_max = tensoes.index(valor) determina a posição da lista (no caso a 1ª);
    c. utilizamos a posição 1 para obter a data correspondente da medição:
        i. datas[idx_max] "05/05/2026 14:44"
2. Somente por meio do .index é possível apontar o local correto no gráfico, por ele sabemos o valor máximo e
o mais importante, quando ele ocorreu;
3. Em tese: 
    a. max(tensoes) qual é o maior valor (min(tensoes) para o valor mínimo);
    b. tensoes.index(valor_max) em que posição da lista o valor está;
    c. datas[idx_max] qual data está relacionada a esta posição.
"""

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

# ---------- Identificação dos Valores Máximo e Mínimo ----------

valor_max = max(tensoes)
valor_min = min(tensoes)
idx_max = tensoes.index(valor_max)
idx_min = tensoes.index(valor_min)     # ler "Observação"

# ---------- Gráfico com Anotações ----------

plt.figure(figsize=(10, 6))
plt.plot(datas, tensoes, marker="o", color="royalblue", linewidth=2)

plt.annotate(f"Valor Máximo: {valor_max}V",     # referencia o texto que aparece na anotação no gráfico.
             xy=(datas[idx_max], valor_max),    # o ponto exato onde a seta aponta. É a coordenada para o valor máximo do gráfico (xy).
             xytext=(datas[idx_max - 1], valor_max - 40),   # ponto onde o texto fica, no caso 20 unidades acima do valor máximo.
             arrowprops=dict(arrowstyle="->", color="green"),   # propriedades da seta, que poderia ser outro símbolo.
             color="green", fontweight="bold")  # a cor e o peso da anotação (no caso o peso é negrito e a cor verde).

plt.annotate(f"Valor Mínimo: {valor_min}V",     # o mesmo se aplica para os valores mínimos
             xy=(datas[idx_min], valor_min),
             xytext=(datas[idx_min - 1], valor_min + 40),
             arrowprops=dict(arrowstyle="->", color="red"),
             color="red", fontweight="bold")

plt.title("Histórico da Tensão com Anotações")
plt.xlabel("Data e Hora")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.tight_layout()

plt.savefig("grafico_anotacoes.png")
print("Visualização de dados salvo com sucesso!")