# Exercício 36: Primeiros passos utilizando Matplotlib.

"""
Observação:
1. Pelo fato de estar utilizando um subsistema do Windows, 
o WLS não irá abrir uma janela com a visualização de dados automaticamente.
Por isso, será necessário gravar os resultados em formato png. 

"""
import matplotlib.pyplot as plt

x = ["04/05/2026 22:58", "05/05/2026 14:44"]
y = [104.17, 302.08]

plt.plot(x, y)

plt.savefig("grafico.png")