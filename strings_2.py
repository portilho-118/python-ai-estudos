# Exercício 23: continuação da manipulação de strings utilizando strip, split e replace. 

texto = " Motor Elétrico "
print(texto.strip())    # Retira os espaços extras entorno do termo entre aspas. 

texto2 = "motor, bomba, compressor"
print(texto2.split(","))    # Utiliza as vírgulas (poderia ser pontos, ou #) como padrão para criação de uma lista.
                            # Padrão: .split("o termo que será utilizado como base").

texto3 = "motor elétrico"
print(texto3.replace("motor", "bomba"))     # Substitui um termo por outro.
                                            # Padrão: .replace("o termo a ser substituído", "o substituto do termo").