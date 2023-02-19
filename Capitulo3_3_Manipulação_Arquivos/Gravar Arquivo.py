with open("teste.txt", "w") as arquivo:
    # O comando abaixo não funciona (se colocar "r") pois o arquivo não existe, então não tem como ler
    # conteudo = arquivo.read()

    arquivo.write("Se isso não funcionar, eu não sei oq vai")

# Sobrescrever o arquivo (com o "a", o arquivo adiciona o texto ao inves de sobrescrever)
with open("teste.txt", "a") as arquivo:
    arquivo.write("\nFuncionou, aleluia!")