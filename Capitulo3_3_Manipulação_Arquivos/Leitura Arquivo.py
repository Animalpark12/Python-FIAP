# Com "rb" retorna o valor em bytes
# Se usar o readlines, o arquivo retorna como um list
with open ("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da váriavel: ", type(conteudo))
print("Conteúdo do arquivo: ", conteudo)