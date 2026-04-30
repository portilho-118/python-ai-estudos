# Exercício 18: atualização do sistema de calculo de elétrica utilizando listas.

from funcoes_eletrica import potencia, corrente, tensao, resistencia
historico = []

while True:
    print("\n=== Sistema de Cálculo Elétrico ===\n")
    print("1. Cálculo de Potência")
    print("2. Cálculo de Corrente")
    print("3. Cálculo de Tensão")
    print("4. Cálculo de Resistência")
    print("5. Ver o histórico de medições")
    print("0. Sair do Sistema")

    opcao = input(str("\nEscolha uma opção: "))

    if opcao == "1":
        valor_tensao = float(input("Digite a tensão em volts: "))
        valor_corrente = float(input("Digite a corrente em amperes: "))
        resultado = potencia(valor_tensao, valor_corrente)
        print(f"Potência: {round(resultado, 2)} watts.")
        historico.append(resultado)
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "2":
        valor_potencia = float(input("Digite a potência em Watts: "))
        valor_tensao = float(input("Digite a tensão em volts: "))
        resultado = potencia(valor_potencia, valor_tensao)
        print(f"Corrente: {round(resultado, 2)} amperes.")
        historico.append(resultado)
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "3":
        valor_potencia = float(input("Digite a potência em Watts: "))
        valor_corrente = float(input("Digite a corrente em amperes: "))
        resultado = tensao(valor_potencia, valor_corrente)
        print(f"Tensão {round(resultado, 2)} volts.")
        historico.append(resultado)
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "4":
        valor_tensao = float(input("Digite a tensão em volts: "))
        valor_corrente = float(input("Digite a corrente em amperes: "))
        resultado = resistencia(valor_tensao, valor_corrente)
        print(f"Resistência {round(resultado, 2)} ohms.")
        historico.append(resultado)
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "5":
        if len(historico) == 0:
            print("Nenhuma medição encontrada.")
        else: 
            print("\n=== Histórico de Medições ===\n")
            for medicao in historico:
                print(f"-> {round(medicao, 2)}")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Digite novamente.")