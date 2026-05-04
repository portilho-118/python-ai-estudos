# Exercício 22: manipulação de strings utilizando .upper, .lower e .strip. 

resposta = input("Deseja continuar? S/N: ")

if resposta.upper() == "S":
    print("Continuando...")
elif resposta.upper() == "N":
    print("Encerrando...")