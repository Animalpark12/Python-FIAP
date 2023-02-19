from Funcoes.Funcoes_Arquivos import *

inventario = {}
opcao = chamarMenu()

while 0 < opcao < 4:

    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        print(exibir())

    opcao = chamarMenu()