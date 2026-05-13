# Exercício 48: primeiro modelo de ML - Classificação de medições elétricas.

"""
Observações:
1. Inicialmente será utilizado um modelo supervisionado. São fornecidos os dados e são apontadas as respostas corretas.
2. A seguir, será trabalhado o modeno não supervisionado. Apenas os dados são fornecidos, e o modelo
aprende sobre sozinho. 
3. Passo a passo do que o programa irá realizar:
    a. Pegar os dados do histórico elétrico (inicialmente artificial);
    b. Rotular cada medição como Normal ou Anormal;
    c. Treinar o modelo com esses dados;
    d. Testar esse modelo com uma medição nova.
4. sklearn.neighbours é um módulo do Scikit-learn que contém algorítimos baseados em vizinhança:
algorítimos que classificam um dado novo comparando os dados mais próximos que já conhece.
5. KNeighborsClassifier é o algorítimo K-Nearest Neighbours (KNN):
K Vizinhos Mais Próximos.
5. O n_neighbours=3 define quantos vizinhos irão participar da "votação" (no caso 3):
    a. Se 2 são "Normal" e 1 é "Anormal" -> Normal
    b. Se 2 são "Anormal" e 1 é "Normal" -> Anormal

"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# ---------- Dados para Treinamento ----------

# [tensao, corrente]:

X_treino = np.array([ # dados de entrada
    [220, 10], [215, 9.5], [225, 10.2], [218, 9.8], [222, 10.1], # definido como normal
    [230, 11], [210, 8.8], [228, 10.8], [212, 9.0], [224, 10.3], # definido como normal
    [54,  6],  [302, 12],  [60,  5.5], [310, 13],  [50,  5], # definido como anormal
    [320, 14], [45,  4.5], [330, 13.5],[48,  5.2], [315, 12.8], # definido como anormal
])

# considere 0 = Normal e 1 = Anormal:

y_treino = np.array([ # rótulo de cada linha do X_treino
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
])

# ---------- Treinamento do Modelo ----------

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_treino, y_treino)

# ---------- Realizando o Teste ----------

testes = np.array([
    [180, 8],
    [240, 11],   
    [100, 7],  
    [220, 10],
    [380, 25],
    [420, 10],
    [127, 10.2],
    [220, 13],
    [380, 2],
    [12.5, 1.3],

])

resultados = modelo.predict(testes)

for i, resultado in enumerate(resultados):
    status = "Normal" if resultado == 0 else "Anormal"
    print(f"Tensão: {testes[i][0]}V | Corrente: {testes[i][1]}A -> {status}")