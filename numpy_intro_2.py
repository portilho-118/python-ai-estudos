# Exercício 29: aplicar o desvio padrão sem a utilização da biblioteca NumPy.

"""
Lembre-se: variancia elevado a 0,5 é o mesmo que fazer a raiz quadrada de variancia.
Ou seja, são matematicamente equivalentes.
Observe que o valor obtido é o mesmo utilizando a biblioteca NumPy: 119.04.  

"""

valores = [220, 127, 380, 440, 220, 127]    # cria a lista valores, com as medidas de tensão.
media = sum(valores) / len(valores)     # a variável "media" realiza a operação de soma dos valores, dividido pelo número de valores (média)
diferencas = [(v - media) ** 2 for v in valores]    # variavel "diferencas" subtrai "v" da média e eleva ao quadrado. 
variancia = sum(diferencas) / len(diferencas)   # "variancia" faz a soma da diferença e divide pelos valores de "v";
desvio = variancia ** 0.5   # "desvio" faz a raiz quadrada da "variancia".
print(f"Desvio padrão: {desvio:.2f}V")