# Exercício 51: Modelo Industrial, utilizando a tensão de 380V e dados de fronteira.

"""
Observações:

1. Considerando um contexto industrial, as tensões consideradas
NORMAIS estariam entre 342V e 418V (10% para mais ou para menos
segundo a ABNT NBR 16149);

2. Já as consideradas como ALERTA, estão dentro da faixa entre 320V
e 342V, ou 418V a 440V;

3. Por último, uma tensão ANORMAL está abaixo de 320V ou acima de 440V;

4. Observando a corrente, para um motor de médio porte à 380V:
    a. Uma corrente normal está entre 10A e 30A;
    b. Alerta: 30A à 40A;
    c. Anormal: abaixo dos 5A ou acima de 40A.

5. Considere a primeira lei de Ohm e a fórmula de potência
para uma melhor compreensão dos limites:

P = V x I x √3

Em um motor que consome 15kW com uma tensão de 380V:
I = P / (V * √3) = 15000 / (380 x 1.73) = 22.8A.

6. É importante organizar os grupos de dados de forma lógica.
Por exemplo, 5 grupos de 10. Desta forma é possível buscar um balanceamento.

7. Vivés de classe: o modelo julgaria mais casos de um agrupamento, e o outro
estaria mal avaliado. A tendência seria adotar como verdadeiro os dados mais
recorrentes;

8. A regra prática para o número de vizinhos é: calcular a raiz quadrada
do número de dados utilizado no modelo. Com 70, seria algo aproximado a
8.3 vizinhos. 

"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# ---------- Dados do Treino ----------

X = np.array([

    # ── Normais: região central ──────────────────
    [380, 20], [375, 18], [385, 22], [378, 19], [382, 21],
    [370, 16], [390, 24], [372, 17], [388, 23], [376, 18],

    # ── Normais: fronteira de tensão ─────────────
    [344, 20], [346, 20], [415, 20], [413, 20], [350, 20],
    [410, 20], [348, 20], [412, 20], [352, 20], [408, 20],

    # ── Normais: fronteira de corrente ───────────
    [380, 11], [380, 12], [380, 28], [380, 29], [375, 10],
    [385, 10], [375, 29], [385, 30], [378, 11], [382, 28],

    # ── Anormais: tensão baixa ───────────────────
    [200, 20], [150, 20], [100, 20], [250, 20], [180, 20],
    [120, 20], [220, 20], [160, 20], [140, 20], [280, 20],

    # ── Anormais: tensão alta ────────────────────
    [500, 20], [550, 20], [480, 20], [520, 20], [600, 20],
    [460, 20], [580, 20], [440, 20], [560, 20], [620, 20],

    # ── Anormais: corrente baixa ─────────────────
    [380, 2],  [375, 3],  [382, 1],  [378, 4],  [380, 2],
    [376, 3],  [384, 1],  [379, 4],  [381, 2],  [377, 3],

    # ── Anormais: corrente alta ──────────────────
    [380, 50], [375, 55], [382, 45], [378, 60], [380, 42],
    [376, 52], [384, 48], [379, 58], [381, 43], [377, 56],
])

y = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # normais centrais
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # normais fronteira tensão
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # normais fronteira corrente
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # anormais tensão baixa
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # anormais tensão alta
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # anormais corrente baixa
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # anormais corrente alta
])

# ---------- Divisão Treino / Teste ----------

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Total de dados: {len(X)}")
print(f"Treino: {len(X_treino)} | Teste: {len(X_teste)}")

# ---------- Treinamento ----------

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_treino, y_treino)

# ---------- Avaliação ----------

y_pred = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, y_pred)
print(f"\nAcurácia: {acuracia * 100:.1f}%")

matriz = confusion_matrix(y_teste, y_pred)
print(f"\nMatriz de Confusão:")
print(f"              Previsto Normal  Previsto Anormal")
print(f"Real Normal        {matriz[0][0]}               {matriz[0][1]}")
print(f"Real Anormal       {matriz[1][0]}               {matriz[1][1]}")

# ---------- Teste de Fronteira ----------

print("\n=== Teste de Fronteira ===\n")
fronteira = np.array([
    [342, 20],  # limite mínimo de tensão
    [340, 20],  # logo abaixo do limite
    [418, 20],  # limite máximo de tensão
    [420, 20],  # logo acima do limite
    [380, 10],  # limite mínimo de corrente
    [380, 8],   # logo abaixo do limite
    [380, 30],  # limite máximo de corrente
    [380, 32],  # logo acima do limite
])

resultados = modelo.predict(fronteira)
for i, r in enumerate(resultados):
    status = "Normal" if r == 0 else "Anormal"
    print(f"Tensão: {fronteira[i][0]}V | Corrente: {fronteira[i][1]}A -> {status}")