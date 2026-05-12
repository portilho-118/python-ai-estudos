# Exercício 47: utilização do método de visualização interativo Gauge utilizando a ferramenta Plotly.

import plotly.graph_objects as go

TENSAO_ATUAL = 215.66
TENSAO_MIN = 187.0
TENSAO_MAX = 253.0

fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=TENSAO_ATUAL,
                title={"text": "Tensão (V)"},
                gauge={
                    "axis": {"range": [0, 300]},
                    "bar": {"color": "royalblue"},
                    "steps": [
                        {"range": [0, TENSAO_MIN], "color": "red"},
                        {"range": [TENSAO_MIN, TENSAO_MAX], "color": "lightgreen"},
                        {"range": [TENSAO_MAX, 300], "color": "orange"},
                    ],
                    "threshold": {
                        "line": {"color": "black", "width": 4},
                        "thickness": 0.75,
                        "value": TENSAO_ATUAL
                    }
                }
                
                ))

fig.update_layout(height=400)
fig.write_html("grafico_gauge.html")
print("Visualização de dados gerado com sucesso.")