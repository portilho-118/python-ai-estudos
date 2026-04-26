# Exercício 4: calculadora de dois números e operações básicas

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
operacao = str(input("Qual operação deseja fazer (escolha as opções: soma, subtracao, divisao ou multiplicacao)? "))

if operacao == "soma":
    resultado = numero_1 + numero_2
    print(f"{numero_1} + {numero_2} = {resultado}.")
elif operacao == "subtracao":
    resultado = numero_1 - numero_2
    print(f"{numero_1} - {numero_2} = {resultado}.")
elif operacao == "divisao":
    resultado = numero_1 / numero_2
    print(f"{numero_1} / {numero_2} = {resultado}.")
elif operacao == "multiplicacao":
    resultado = numero_1 * numero_2
    print(f"{numero_1} x {numero_2} = {resultado}.")
else: print("Operação inválida, por favor escolha uma das opções: soma, subtracao, divisao ou multiplicacao.")