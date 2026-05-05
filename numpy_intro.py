# Exercício 28: introdução ao uso do NumPy como ferramenta matemática. 
# Desvio padrão: é a medida de o quanto os valores em um conjunto se afastam da média.

"""
Cálculo do desvio padrão passo a passo:
1. Calcule a média;
2. Subtrai a média de cada valor;
3. Eleva cada resultado ao quadrado;
4. Calcula a média desses quadrados;
5. Tira a raiz quadrada do valor final.

"""

import numpy as np  # np é apenas um nome dado para poupar código. 
                    # Ao invés de escrever numpy.mean() todas as vezes, basta escrever np.mean().
                    # np é a convenção universal da comunidade Python.

medicoes = np.array([220, 127, 380, 440, 220, 127 ])    # np.array tem a função de definir o intervalo de valores.

print(f"Média: {np.mean(medicoes):.2f}V")   # np.mean realiza a média;
print(f"Máxima: {np.max(medicoes)}V")   # np.max obtém o valor máximo;
print(f"Mínima: {np.min(medicoes)}V")   # np.min define o valor mínimo;
print(f"Desvio padrão: {np.std(medicoes):.2f}V") # np.std efetua o desvio padrão.