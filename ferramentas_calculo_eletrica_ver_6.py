    # Exercício 26: atualização do sistema de cálculo elétrico utilizando o conceito de arquivo.

from funcoes_eletrica import potencia, corrente, tensao, resistencia

def salvar_historico(tipo, valor, unidade):
    with open("historico_medicoes.txt", "a") as arquivo:
        arquivo.write(f"{tipo}: {round(valor, 2)} {unidade}\n") 

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

        try:

            valor_tensao = float(input("Digite a tensão em volts: "))
            valor_corrente = float(input("Digite a corrente em amperes: "))
            resultado = potencia(valor_tensao, valor_corrente)
            print(f"Potência: {round(resultado, 2)} watts.")

            historico.append({
            "tipo": "Potência",
            "valor": resultado,
            "unidade": "watts"
        })
            
            salvar_historico("Potência", resultado, "watts")
            
        except ValueError:
            print("Erro! Digite apenas números.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "2":

        try:

            valor_potencia = float(input("Digite a potência em Watts: "))
            valor_tensao = float(input("Digite a tensão em volts: "))
            resultado = corrente(valor_potencia, valor_tensao)
            print(f"Corrente: {round(resultado, 2)} amperes.")

            historico.append({
            "tipo": "Corrente",
            "valor": resultado,
            "unidade": "amperes"
        })  
        
            salvar_historico("Corrente", resultado, "amperes")

        except ValueError:
            print("Erro! Digite apenas números.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "3":

        try:

            valor_potencia = float(input("Digite a potência em Watts: "))
            valor_corrente = float(input("Digite a corrente em amperes: "))
            resultado = tensao(valor_potencia, valor_corrente)
            print(f"Tensão {round(resultado, 2)} volts.")

            historico.append({
            "tipo": "Tensão",
            "valor": resultado,
            "unidade": "volts"
        })
            
            salvar_historico("Tensão", resultado, "volts")

        except ValueError:
            print("Erro! Digite apenas números.")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "4":

        try:

            valor_tensao = float(input("Digite a tensão em volts: "))
            valor_corrente = float(input("Digite a corrente em amperes: "))
            resultado = resistencia(valor_tensao, valor_corrente)
            print(f"Resistência {round(resultado, 2)} ohms.")
        
            historico.append({
            "tipo": "Resistência",
            "valor": resultado,
            "unidade": "ohms"
        })
            
            salvar_historico("Resistência", resultado, "ohms")
            
        except ValueError:
            print("Erro! Digite apenas números.")           
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "5":
        if len(historico) == 0:
            print("Nenhuma medição encontrada.")
        else: 
            print("\n=== Histórico de Medições ===\n")
            for medicao in historico:
                print(f"{medicao['tipo']}: {round(medicao['valor'], 2)} {medicao['unidade']}")
        input("\nPressione Enter caso deseje realizar outro cálculo.")

    elif opcao == "0":
        confirmacao = input("Tem certeza que deseja sair do sistema? S/N: ")
        if confirmacao.upper() == "S":
            print("Encerrando o sistema...")
            break
        else:
            print("Retornando ao menu...")

    else:
        print("Opção inválida. Digite novamente.")