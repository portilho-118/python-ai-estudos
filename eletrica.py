# Exercício 8: cálculo simples de potência elétrica 

def potencia(tensao, corrente):
    p = tensao * corrente
    print(f"Potência: {p} Watts")

potencia(220, 5)
potencia(127, 10)