# Exercício 50: testando valores na fronteira do modelo.

"""
Observações:

1. Qundo se implementa um modelo de ML, deve-se obedecer determinados
passos críticos. Um deles consiste na validação do modelo. Alguns testes
são:
    a. Teste de Fronteira: verifica-se os valores no limite entre Normal
    e anormal;
    b. Teste de estresse: checa valores extremos com base nos dados
    fornecidos;
    c. Teste de casos reais: utilização de dados que não estão
    inclusos no modelo.
2. Região de baixa densidade: uma área no espaço de dados onde 
o modelo não tem exemplos de treino suficientes para decidir
com confiança. Formas de solucionar:
    a. Identificar as regiões problemáticas;
    b. Coletar mais dados nessas regiões;
    c. Retreinar o modelo.
    d. Validar novamente.

"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# ---------- Dados de Treino ----------

X_treino = np.array([
    [220, 10], [215, 9.5], [225, 10.2], [218, 9.8], [222, 10.1],
    [230, 11], [210, 8.8], [228, 10.8], [212, 9.0], [224, 10.3],
    [219, 9.7],[223, 10.4],[216, 9.3], [226, 10.6],[221, 9.9],
    [54,  6],  [302, 12],  [60,  5.5], [310, 13],  [50,  5],
    [320, 14], [45,  4.5], [330, 13.5],[48,  5.2], [315, 12.8],
    [58,  6.2],[308, 12.3],[52,  5.8], [325, 13.2],[55,  5.5],
])

y_treino = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
])

# ---------- Treinamento ----------

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_treino, y_treino)

# ---------- Testando a Fronteira ----------

fronteira = np.array([
    [186, 9],
    [187, 9],
    [188, 9],
    [190, 9],
    [200, 9],
    [210, 9],
])

resultados = modelo.predict(fronteira)

print("=== Teste de Fronteira ===\n")
for i, r in enumerate(resultados):
    status = "Normal" if r == 0 else "Anormal"
    print(f"Tensão: {fronteira[i][0]}V | Corrente: {fronteira[i][1]}A -> {status}")