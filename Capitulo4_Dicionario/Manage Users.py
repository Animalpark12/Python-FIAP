from Capitulo4_Dicionario.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":

    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios, input("Qual o login deverá ser pesquisado?: ").upper())
    elif opcao == "E":
        excluir(usuarios, input("Digite o login para a exclusão: ").upper())
    elif opcao == "L":
        listar(usuarios)

    opcao = perguntar()
