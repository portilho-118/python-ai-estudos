# Exercício 53: Regressão linear para previsão de potência elétrica

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# ---------- Dados ----------
# [tensão, corrente] -> potência

X = np.array([
    [380, 20], [375, 18], [385, 22], [378, 19], [382, 21],
    [370, 16], [390, 24], [372, 17], [388, 23], [376, 18],
    [360, 15], [395, 25], [368, 16], [392, 24], [374, 17],
    [400, 26], [365, 15], [387, 22], [373, 18], [383, 21],
])

# Potência Real = tesão x corrente
y = np.array([v*i for v, i in X]) # Por meio desse código é possível obter os valores de potência automaticamente.

# ---------- Divisão Treino/Teste ----------

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Total de dados: {len(X)}")
print(f"Treino: {len(X_treino)} | Teste: {len(X_teste)}")

# ---------- Treinamento ----------

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# ---------- Avaliação ----------

y_pred = modelo.predict(X_teste)

mse = mean_absolute_error(y_teste, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_teste, y_pred)

print(f"\nErro Médio (MSE):  {mse:.2f}W²")
print(f"Erro Médio (RMSE): {rmse:.2f}W ")
print(f"R² Score:          {r2:.4f}")

# ---------- Teste ----------

print("\n=== Previsões ===\n")
testes = np.array([
    [380, 20],
    [375, 18],
    [400, 25],
    [360, 15],
    [390, 22],
    [370, 17],
    [385, 21],
    [395, 24],
    [365, 16],
    [382, 19],
    [378, 20],
    [392, 23],
])

previsoes = modelo.predict(testes)
for i, p in enumerate(previsoes):
    real = testes[i][0] * testes[i][1]
    erro_w = abs(p-real)
    erro_pct = (erro_w / real) * 100
    print(f"Tensão: {testes[i][0]}V | Corrente: {testes[i][1]}A")
    print(f"  Previsto: {p:.2f}W | Real: {real}W | Erro: {erro_w:.2f}W -> ({erro_pct:.2f}%)\n")