# Exercício 10: cálculo de potência com input de valores pelo usuário

def potencia (tensao, corrente):
    p = tensao * corrente
    return p

tensao = float(input("Digite a tensão do equipamento em volts: "))
corrente = float(input("Digite a corrente do equipamento em amperes: "))

resultado = potencia(tensao, corrente)

if resultado < 500:
    print(f"Potência: {resultado} Watts - Baixa potência")
elif resultado < 2000:
    print(f"Potência: {resultado} Watts - Potência média")
else:    print(f"Potência: {resultado} Watts - Alta potência")

