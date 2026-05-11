# Exercício 45: Geração de dados sintéticos para enriquecimento do histórico de medidas.

"""
Observação:
1. variavel = round(randon.uniform(a, b)) gera um número aleatório decimal entre os valores "a" e "b"
previamente definidos;

"""

import random
from datetime import datetime, timedelta

# ---------- Configurações ----------

TOTAL_MEDICOES = 30
DATA_INICIO = datetime(2026, 5, 11, 8, 0)

# Utilizando faixas realistas para uma instalação industrial:

TENSAO_MEDIA = 220
CORRENTE_MEDIA = 10
VARIACAO = 0.15 # ou 15% da variação

# ---------- Gerando os dados ----------

with open("historico_medicoes.txt", "a") as arquivo:
    for i in range(TOTAL_MEDICOES):
        data_hora = DATA_INICIO + timedelta(minutes=i * 30)
        data_str = data_hora.strftime("%d/%m/%Y %H%M")

        tensao = round(random.uniform( 
            TENSAO_MEDIA * (1 - VARIACAO),
            TENSAO_MEDIA * (1 + VARIACAO)
        ), 2)

        corrente = round(random.uniform(
            CORRENTE_MEDIA * (1 - VARIACAO),
            CORRENTE_MEDIA * (1 + VARIACAO)
        ), 2)

        potencia = round(tensao * corrente, 2)
        resistencia = round(tensao / corrente, 2)

        arquivo.write(f"[{data_str}] Tensão: {tensao} volts\n")
        arquivo.write(f"[{data_str}] Corrente: {corrente} amperes\n")
        arquivo.write(f"[{data_str}] Potência: {potencia} watts\n")
        arquivo.write(f"[{data_str}] Resistência: {resistencia} ohms\n")

print(f"{TOTAL_MEDICOES * 4} registros adicionados ao histórico.")