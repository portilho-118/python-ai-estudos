# Exercício 3: cálculo de IMC com input

nome = str(input("Qual é o seu nome? "))
peso = float(input("Qual é o seu peso (kg)? "))
altura = float(input("Qual é a sua altura (m)? "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "abaixo do peso, procure ajuda especializada."
elif imc < 24.9:
    classificacao = "peso normal!"
elif imc < 29.9:
    classificacao = "sobrepeso, fique atento!"
else: "obesidade, procure ajuda médica."


print(f"Olá, {nome}. De acordo com os cálculos, o seu IMC é de {round(imc, 2)}. Neste valor você está classificado como {classificacao}.")