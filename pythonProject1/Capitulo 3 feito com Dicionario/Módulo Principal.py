from Funcoes.Funcoes_Dicionário import *

material = {}
opcao = perguntar()

while opcao == "I" or opcao == "E" or opcao == "P" or opcao == "D":
    if opcao == "I":
        print("Preenchendo...")
        preencherDicionario(material)
    elif opcao == "E":
        print("Exibindo todo o inventário: ")
        listarDicionario(material)
    elif opcao == "P":
        print("Exibindo...")
        pesquisarDicionario(material, int(input("Digite o número serial do objeto: ")))
    elif opcao == "D":
        excluir(material, int(input("Digite o número serial do objeto para ser excluido: ")))

    opcao = perguntar()
