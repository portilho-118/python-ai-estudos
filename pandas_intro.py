# Exercício 30: introdução ao Pandas por meio da estrutura DataFrame.

"""

Observações:

1. pd é o nome consagrado do pandas na comunidade Python;
2. "dados" é a variável que irá guardas as informações das medições;
3. Chaves e valores (strings), entre aspas. Os valores devem estar entre colchetes;
4. Não esquecer da vírgula para inserir o próximo conjunto de dados;
5. Valores float e int não utiliza aspas;
6. O último conjunto não acompanha vírgula;
7. df é a variável que guarda a estrutura pd.DataFrame e utiliza (dados) como fonte;
8. As chaves dos conjuntos correspondem o cabeçalho de cada coluna;
9. Ao imprimir o resultado, uma coluna apontando a numeração de cada linha é incorporada a planilha. 

"""

import pandas as pd

dados = {

"tipo": ["Potência", "Corrente", "Tensão", "Resistência"],
"valor": [2640, 9.45, 380, 25.4],
"unidade": ["watts", "amperes", "volts", "ohms"]

}

df = pd.DataFrame(dados)
print(df)