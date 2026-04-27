# Exercício 5: tabuada de um número simples

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
