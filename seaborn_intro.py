# Exercício 43: Introdução ao uso do Seaborn.

"""
Observação:
1. O Seaborn foi desenvolvido com a intenção de trabalhar com dados estatísticos.
Baseado no Metplotlib, a biblioteca oferece recursos facilitados para a criação de
boxplot, heatmap e violinplot em poucas linhas de código.

2. O boxplot é um gráfico estatístico que resume a distribuição de um conjunto de valores
em uma "caixa". São exibidos 5 informações ao mesmo tempo para o usuário. Recurso muito comum
em ciências de dados, e utiliado para treinar modelos de IA para compreensão da distribuição
dos dados.

"""

import seaborn as sns
import matplotlib.pyplot as plt

# ----------  Leitura do Histórico ----------

dados = {"tipo": [], "valor": []}

with open("historico_medicoes.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith("["):
            resto = linha [18:]
            partes = resto.split(":")
            if len(partes) < 2:
                continue
            tipo = partes[0].strip()
            valor = float(partes[1].strip().split(" ")[0])

            dados["tipo"].append(tipo)
            dados["valor"].append(valor)

# ---------- Gráfico utilizando Seaborn ----------

plt.figure(figsize=(10, 6))
sns.boxplot(x="tipo", y="valor", data=dados, palette="Set2")

""" 
-> Ao invés de passar os eixos x e y como listas separadas,
você passa o dicionário inteiro no "data" e diz quais
chaves utilizar.

-> palette="Set2" é uma das paletas de cores adotadas pelo Seaborn.
Muito útil, pois ao invés de usar color="royalblue" em cada elemento,
o Seaborn distribui as cores automaticamente por categoria.
                                                      
"""

plt.title("Distribuição dos valores por Tipo de Medição")
plt.xlabel("Tipo")
plt.ylabel("Valor")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("grafico_seaborn.png")
print("Visualização de dados gerado com sucesso!")