import json
import os


def chamarMenu():
    opcao = int(input("Digite: " +
                      "\n<1> - Para registrar um ativo" +
                      "\n<2> - Para exibir ativos armazenados" +
                      "\nComando: "))
    return opcao


def lerArquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arqJson:
            dicionario = json.load(arqJson)
    else:
        dicionario = {}
    return dicionario


def gravarArquivo(dicionario, arquivo):
    with open(arquivo, "w") as arqJson:
        json.dump(dicionario, arqJson)


def registrar(dicionario, arquivo):
    resposta = "S"
    while resposta == "S":
        numeroPatrimonial = int(input("Digite o número patrimonial: "))
        dicionario[numeroPatrimonial] = [input("Digite a data da atualização: "),
                                         input("Digite a descrição: "),
                                         input("Digite o departamento: ").upper()]
        resposta = input("Digite <S> para continuar: ").upper()
        gravarArquivo(dicionario, arquivo)
    return "JSON criado com sucesso!!!"


def exibir(arquivo):
    dicionario = lerArquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data..........: ", dado[0])
        print("Descrição.....: ", dado[1])
        print("Departamento..: ", dado[2])
        print("")
