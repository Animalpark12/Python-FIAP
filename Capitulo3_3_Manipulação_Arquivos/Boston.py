with open("economic-indicators.csv", "r") as boston:
    totalVoos = 0
    maior = 0
    totalPassageiros = 0
    maiorMediaDiaria = 0
    anoUsuario = input("Qual ano deseja pesquisar?: ")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        totalVoos += float(lista[3])
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if anoUsuario == lista[0]:
            totalPassageiros += float(lista[2])
            if float(lista[5]) > float(maiorMediaDiaria):
                maiorMediaDiaria = lista[5]
                mesMaiorDiaria = lista[1]
    print("O total de voos é: ", totalVoos)
    print("O mês/ano de maior movimento no aeroporto foi: ", str(mes), "/", str(ano))
    print("O total de passageiros do ano", anoUsuario, "foi de", totalPassageiros)
    print("O mês do ano", anoUsuario, "com maior média para diária de hotel foi de", mesMaiorDiaria)