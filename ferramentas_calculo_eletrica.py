# Exercício 13: criar um menu para acessar um conjunto de fórmulas úteis para elétrica.

from funcoes_eletrica import potencia, corrente, tensao, resistencia

while True :
    print("\n=== Sistema de Cálculo Elétrico === \n")
    print("1. Cálculo de potência")
    print("2. Cálculo de corrente")
    print("3. Cálculo de tensão")
    print("4. Cálculo de resistência")
    print("0. Sair do sistema")

    opcao = input(str("\nEscolha uma opção: "))

    if opcao == "1":
        valor_tensao = float(input("Digite a tensão em volts: "))
        valor_corrente = float(input("Digite a corrente em amperes: "))
        resultado = potencia(valor_tensao, valor_corrente)
        print(f"Potência: {round(resultado, 2)} Watts.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "2":
        valor_potencia = float(input("Digite a potência em Watts: "))
        valor_tensao = float(input("Digite a tensão em volts: "))
        resultado = corrente(valor_potencia, valor_tensao)
        print(f"Corrente {round(resultado, 2)} Amperes.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")
    
    elif opcao == "3":
        valor_potencia = float(input("Digite aqui a potência em Watts: "))
        valor_corrente = float(input("Digite aqui a corrente em amperes: "))
        resultado = tensao(valor_potencia, valor_corrente)
        print(f"Tensão {round(resultado, 2)} Volts.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")
    
    elif opcao == "4":
        valor_tensao = float(input("Digite aqui a tensão em volts: "))
        valor_corrente = float(input("Digite aqui a corrente em amperes: "))
        resultado = resistencia(valor_tensao, valor_corrente)
        print(f"Resistência {round(resultado, 2)} Ohms.")
        input("\nPressione Enter para continuar.")
    
    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Digite novamente.")