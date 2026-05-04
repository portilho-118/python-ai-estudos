# Exercício 25: criação e manipulação de arquivos utilizando o comando "with open as".

# Para escrever utiliza-se with open ("arquivo pretendido", "a") as nome do arquivo.
# O uso do "a" significa append, ou seja "modo append" (adiciona sem apagar o que já existe).

with open("teste.txt", "a") as arquivo:
    arquivo.write("Potência: 2640 watts\n")
    arquivo.write("Corrente: 9.45 amperes\n")

# Para ler utiliza-se "r" (read) ao invés do "a".

with open("teste.txt", "r") as arquivo: # O "r" irá solicitar a ação de leitura do arquivo.
    conteudo = arquivo.read() # A variável "conteudo" guarda o texto lido do arquivo, ou seja, uma memória.
                              # Se utiliza .read() (com parênteses vazio) na intenção de ler todo o arquivo.
                              # Pode-se incluir um valor, por exemplo (100), para ler os primeiros 100 caracteres do arquivo.
    print(conteudo)           # O print(conteudo) irá exibir tudo que foi lido.