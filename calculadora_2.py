# Exercício 7: calculadora aperfeiçoada utilizando (while)

numero_1 = float(input("Digite o primeiro número:  "))
numero_2 = float(input("Digite o segundo número:  "))

while True:

    operacao = str(input("Qual operação você deseja fazer? Escolha entre: soma, " \
    "subtracao, divisao ou multiplicacao: "))
    if operacao == "soma":
       resultado = numero_1 + numero_2
       print(f"{numero_1} + {numero_2} = {round(resultado, 2)}.")

    elif operacao == "subtracao":
        resultado = numero_1 - numero_2
        print(f"{numero_1} - {numero_2} = {round(resultado, 2)}.")

    elif operacao == "divisao":
        resultado = numero_1 / numero_2
        print(f"{numero_1} / {numero_2} = {round(resultado, 2)}.")

    elif operacao == "multiplicacao":
        resultado = numero_1 * numero_2
        print(f'{numero_1} x {numero_2} = {round(resultado, 2)}.')

    else: print("Operação inválida, por favor escolha uma das opções: soma, subtracao, divisao ou multiplicacao.")
    
    continuar = str(input("Deseja realizar uma nova operação? Y/N: "))
    if continuar == "Y":
        numero_1 = float(input("Digite o primeiro número:  "))
        numero_2 = float(input("Digite o segundo número:  "))
    elif continuar == "N":
        print("Encerrando a calculadora.")
        break