# Exercício 52: Classificação multiclasse - Normal, Alerta e Anormal

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# ---------- Dados de Treino ----------

"""
[tensao, corrente]

0 = Normal -> 342-418V, 10-30A
1 = Alerta -> 320-342V ou 418-440V, 8-10A ou 30-40A
2 = Anormal -> abaixo de 320V ou acima de 440V, abaixo de 5A ou acima de 40A

"""

X = np.array([
    # Normais
    [380, 20], [375, 18], [385, 22], [378, 19], [382, 21],
    [370, 16], [390, 24], [372, 17], [388, 23], [376, 18],

    #Alerta - Tensão Baixa
    [335, 20], [330, 20], [325, 20], [338, 20], [322, 20],
    [340, 20], [328, 20], [332, 20], [336, 20], [324, 20],

    # Alerta - Tensão Alta
    [425, 20], [430, 20], [435, 20], [422, 20], [438, 20],
    [420, 20], [428, 20], [432, 20], [424, 20], [436, 20],

    # Alerta - Corrente Baixa
    [380, 9],  [380, 8],  [375, 9],  [385, 8],  [378, 9],
    [382, 8],  [376, 9],  [384, 8],  [379, 9],  [381, 8],

    # Alerta - Corrente Alta
    [380, 35], [380, 38], [375, 33], [385, 36], [378, 34],
    [382, 37], [376, 32], [384, 39], [379, 31], [381, 36],

    # Anormais - Tensão Baixa
    [200, 20], [150, 20], [100, 20], [250, 20], [180, 20],
    [120, 20], [220, 20], [160, 20], [140, 20], [280, 20],

    # Anormais - Tensão Alta
    [500, 20], [550, 20], [480, 20], [520, 20], [600, 20],
    [460, 20], [580, 20], [440, 20], [560, 20], [620, 20],

    # Anormais - Corrente
    [380, 2],  [375, 3],  [382, 1],  [378, 4],  [380, 2],
    [380, 50], [375, 55], [382, 45], [378, 60], [380, 42],
])

y = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # Normal
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Alerta Tensão Baixa
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Alerta Tensão Alta
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Alerta Corrente Baixa
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Alerta Corrente Alta
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Anormal Tensão Baixa
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Anormal Tensão Alta
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Anormal Corrente
])

# ---------- Divisão Treino/Teste ----------

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Total de Dados: {len(X)}")
print(f"Treino: {len(X_treino)} | Teste: {len(X_teste)}")

# ---------- Treinamento ----------

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_treino, y_treino)

# ---------- Avaliação ----------

y_pred = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, y_pred)
print(f"\nAcuracia: {acuracia * 100:.1f}%")

matriz = confusion_matrix(y_teste, y_pred)
print(f"\nMatriz de Confusão:")
print(f"{'':15} {'Prev. Normal':>12} {'Prev. Alerta':>12} {'Prev. Anormal':>13}")
print(f"{'Real Normal':15} {matriz[0][0]:>12} {matriz[0][1]:>12} {matriz[0][2]:>13}")
print(f"{'Real Alerta':15} {matriz[1][0]:>12} {matriz[1][1]:>12} {matriz[1][2]:>13}")
print(f"{'Real Anormal':15} {matriz[2][0]:>12} {matriz[2][1]:>12} {matriz[2][2]:>13}")

# ---------- Teste ----------

print("\n=== Teste de Classificação ===\n")
testes = np.array([
    [380, 20],  # Normal
    [335, 20],  # Alerta tensão baixa
    [425, 20],  # Alerta tensão alta
    [380, 9],   # Alerta corrente baixa
    [380, 35],  # Alerta corrente alta
    [200, 20],  # Anormal tensão baixa
    [500, 20],  # Anormal tensão alta
    [380, 2],   # Anormal corrente
])

resultados = modelo.predict(testes)
labels = {0: "Normal", 1: "Alerta,", 2: "Anormal"}

for i, r in enumerate(resultados):
    print(f"Tensão: {testes[i][0]}V | Corrente: {testes[i][1]}A -> {labels[r]}")