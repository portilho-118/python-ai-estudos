# Exercício 2: cálculo de aposentadoria com input de dados
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

ano_aposentadoria = 65
anos_restantes = ano_aposentadoria - idade

print(f"Olá, {nome}! Faltam {anos_restantes} anos para você se aposentar.")