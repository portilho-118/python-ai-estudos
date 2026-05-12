# Exercício 46: Desenvolvendo subplots interativos utilizando a ferramenta Plotly.

"""
Observações:
1. shared_xaxes=True possui a função de compartilhar o eixo X nos três gráficos.
Dessa forma, ao ampliar os gráficos em um período, exibindo Tensão, por exemplo,
os gráficos de Corrente e Potência vão, automaticamente, para o mesmo período.

"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# ---------- Leitura do Histórico ----------

datas_tensao, horas_tensao, tensoes = [], [], []
datas_corrente, horas_corrente, correntes = [], [], []
datas_potencia, horas_potencia, potencias = [], [], []

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
            data_completa = linha[1:17]
            data = data_completa.split(" ")[0]
            hora = data_completa.split(" ")[1]

            if tipo == "Tensão":
                datas_tensao.append(data)
                horas_tensao.append(hora)
                tensoes.append(valor)
            elif tipo == "Corrente":
                datas_corrente.append(data)
                horas_corrente.append(hora)
                correntes.append(valor)
            elif tipo == "Potência":
                datas_potencia.append(data)
                horas_potencia.append(hora)
                potencias.append(valor)

# ---------- Criação dos Subplots ----------

fig = make_subplots(rows=3, cols=1,
                    subplot_titles=("Tensão (V)", "Corrente (A)", "Potência (W)"),
                    shared_xaxes=True)

fig.add_trace(go.Scatter(x=datas_tensao, y=tensoes,
                         mode="lines+markers", name="Tensão",
                         line=dict(color="royalblue"),
                         customdata=list(zip(datas_tensao, horas_tensao)),
                         hovertemplate="Data: %{customdata[0]}<br>Hora: %{customdata[1]}<br>Valor: %{y} V<extra></extra>"
                        ), row=1, col=1)

fig.add_trace(go.Scatter(x=datas_corrente, y=correntes,
                         mode="lines+markers", name="Corrente",
                         line=dict(color="tomato"),
                         customdata=list(zip(datas_corrente, horas_corrente)),
                        hovertemplate="Data: %{customdata[0]}<br>Hora: %{customdata[1]}<br>Valor: %{y} A<extra></extra>"
                         ), row=2, col=1)

fig.add_trace(go.Scatter(x=datas_potencia, y=potencias,
                         mode="lines+markers", name="Potência",
                         line=dict(color="seagreen"),
                         customdata=list(zip(datas_potencia, horas_potencia)),
                         hovertemplate="Data: %{customdata[0]}<br>Hora: %{customdata[1]}<br>Valor: %{y} W<extra></extra>"
                         ), row=3, col=1)

fig.update_layout(title="Monitoramento Elétrico - Visão Geral", height=800)

fig.write_html("grafico_subplots_plotly.html")
print("Subplots interativos gerados com sucesso!")