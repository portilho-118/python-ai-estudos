# Exercício 45: Geração de dados sintéticos para enriquecimento do histórico de medidas.

"""
Observação:
1. variavel = round(randon.uniform(a, b)) gera um número aleatório decimal entre os valores "a" e "b"
previamente definidos;

"""

import random
from datetime import datetime, timedelta

# ---------- Configurações ----------

TOTAL_MEDICOES = 10
DIAS = (4, 5, 6, 7, 8)

# Utilizando faixas realistas para uma instalação industrial:

TENSAO_MEDIA = 220
CORRENTE_MEDIA = 10
VARIACAO = 0.15 # ou 15% da variação

# ---------- Gerando os dados ----------

with open("historico_medicoes.txt", "a") as arquivo:
    for dia in DIAS:
        for i in range(TOTAL_MEDICOES):
            data_hora = datetime(2026, 5, dia, 8, 0) + timedelta(hours=i * 1.5)
            data_str = data_hora.strftime("%d/%m/%Y %H:%M")

        tensao = round(random.uniform(TENSAO_MEDIA * (1 - VARIACAO), TENSAO_MEDIA * (1 + VARIACAO)), 2)
        corrente = round(random.uniform(CORRENTE_MEDIA * (1 - VARIACAO), CORRENTE_MEDIA * (1 + VARIACAO)), 2)
        potencia = round(tensao * corrente, 2)
        resistencia = round(tensao / corrente, 2)

        arquivo.write(f"[{data_str}] Tensão: {tensao} volts\n")
        arquivo.write(f"[{data_str}] Corrente: {corrente} amperes\n")
        arquivo.write(f"[{data_str}] Potência: {potencia} watts\n")
        arquivo.write(f"[{data_str}] Resistência: {resistencia} ohms\n")

print(f"{TOTAL_MEDICOES * len(DIAS) * 4} registros adicionados ao histórico.")