# Exercício 11: separar funções em arquivos diferentes utilizando o cálculo de potência como base (arquivo 1)
# Exercício 12: adicionar outras fórmulas para tornar o programa mais robusto

def potencia(tensao, corrente):
    return tensao * corrente

def corrente(potencia, tensao):
    return potencia / tensao

def tensao(potencia, corrente):
    return potencia / corrente

def resistencia(tensao, corrente):
    return tensao / corrente