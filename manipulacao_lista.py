# Exercício 16: manipulação de valores em listas utilizando append, insert, remove e pop.

tensoes = [220, 127, 380]

tensoes.append(440) # .append adiciona um valor ao final
print(tensoes)

tensoes.remove(127) # .remove utilizando o valor como referência
print(tensoes)

tensoes.pop() # .pop remove o último valor da lista
print(tensoes)

tensoes.insert(0, 127) # insert é usado para inserir um valor em qualquer posição .insert (posição desejada, valor)
print(tensoes)