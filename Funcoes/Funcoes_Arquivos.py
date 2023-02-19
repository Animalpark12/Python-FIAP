def chamarMenu():
    escolha = int(input("Digite: " +
                        "\n<1> - Registrar ativo" +
                        "\n<2> - Persistir em arquivo" +
                        "\n<3> - Exibir arquivos armazenados" +
                        "\nComando: "))
    return escolha


def registrar(dicionario):
    resposta = "S"
    while resposta == "S":
        numeroPatrimonial = int(input("Digite o número patrimonial: "))
        dicionario[numeroPatrimonial] = [input("Digite a data de atualização: "),
                                         input("Digite a descrição: "),
                                         input("Digite o departamento: ").upper()]
        resposta = input("Digite <S> para continuar: ").upper()


def persistir(dicionario):
    with open("inventarios.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(str(chave) + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + ";")
    return "Persistido com sucesso"

def exibir():
    with open("inventarios.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas