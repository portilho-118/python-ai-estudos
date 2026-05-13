# Exercício 49: Avaliação do modelo de ML, compreendendo o que é acurácia e matriz de confusão.

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# ---------- Dados ----------

X = np.array([
    [220, 10], [215, 9.5], [225, 10.2], [218, 9.8], [222, 10.1],
    [230, 11], [210, 8.8], [228, 10.8], [212, 9.0], [224, 10.3],
    [219, 9.7],[223, 10.4],[216, 9.3], [226, 10.6],[221, 9.9],
    [54,  6],  [302, 12],  [60,  5.5], [310, 13],  [50,  5],
    [320, 14], [45,  4.5], [330, 13.5],[48,  5.2], [315, 12.8],
    [58,  6.2],[308, 12.3],[52,  5.8], [325, 13.2],[55,  5.5],
])

y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
])

# ---------- Divisão Treino/Teste ----------

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Total de dados: {len(X)}")
print(f"Treino: {len(X_treino)} | Teste: {len(X_teste)}")

# ---------- Treinamento ----------

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_treino, y_treino)

# ---------- Avaliação ----------

y_pred = modelo.predict(X_teste)

acuracia = accuracy_score(y_teste, y_pred)
print(f"\nAcurácia: {acuracia * 100:.1f}%")

matriz = confusion_matrix(y_teste, y_pred)
print(f"\nMatriz de Confusão:")
print(f"              Previsão Normal  Previsão Anormal")
print(f"Real Normal        {matriz[0][0]}               {matriz [0][1]}")
print(f"Real Anormal       {matriz[1][0]}               {matriz[1][1]}")