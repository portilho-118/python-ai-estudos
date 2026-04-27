# Continuação exercício 11: separar funções em arquivos diferentes utilizando o cálculo de potência como base (arquivo 2)

from funcoes_eletrica import potencia 
# 'from' acessa o código localizado em outro arquivo;
# 'import' acessa a função específica daquele código.

tensao = float(input("Digite a tensão em volts: "))
corrente = float(input("Digite a corrente em amperes: "))

resultado = potencia(tensao, corrente)

if resultado < 500:
    print(f"Potência: {resultado} Watts - Baixa potência.")
elif resultado < 2000:
    print(f"Potência: {resultado} Watts - Média potência.")
else:
    print(f"Potência: {resultado} Watts - Alta potência.")