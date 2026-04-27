# Exercício 9: cálculo de potência utilizando return

def potencia (tensao, corrente):
    p = tensao * corrente
    return p

p1 = potencia(5, 1.3)

if p1 < 500:
    print(f"Potência: {p1} Watts - Baixa potência")

elif p1 < 2000:
    print(f"Potência: {p1} Watts - Potência média")

else:
    print(f"Potência: {p1} Watts - Alta potência")