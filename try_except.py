# Exercício 20: tratamento de erros utilizando try e except.

try:
    valor = float(input("Digite um número: "))
    print(f'Valor digitado: {valor}')
except ValueError:
    print("Erro! Digite apenas números.")