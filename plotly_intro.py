# Exercício 44: Introdução ao Plotly, desenvolvimento de um gráfico de tensão interativo

import plotly.graph_objects as go

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

# ---------- Gráfico Plotly ----------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=datas,
    y=tensoes,
    mode="lines+markers",
    name="Tensão (V)",
    line=dict(color="royalblue", width=2),
    marker=dict(size=8)
))

fig.update_layout(
    title="Histórico da Tensão – Fráfico Interativo",
    xaxis_title="Data e Hora",
    yaxis_title="Tensão (V)",
    hovermode="closest"
)

fig.update_traces(
    hovertemplate="<b>%{x}</b><br>Tensão %{y}V<extra></extra>"
)

fig.write_html("grafico_plotly.html")
print("Gráfico interativo gerado com sucesso! Acesse em: grafico_plotly.html")