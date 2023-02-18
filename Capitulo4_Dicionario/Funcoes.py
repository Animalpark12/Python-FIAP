def perguntar():
    resposta = input("O que deseja realizar? \n"
                     +
                     "<I> - Para Inserir um usuário \n"
                     +
                     "<P> - Para Pesquisar um usuário \n"
                     +
                     "<E> - Para Excluir um usuário \n"
                     +
                     "<L> - Para Listar um usuário \n"
                     +
                     "Comando: ").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                         input("Digite a última data de acesso: "),
                         input("Digite a hora do login: "),
                         input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome............: " + lista[0])
        print("Último acesso...: " + lista[1])
        print("Última estação..: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto deletado com sucesso!")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto abaixo ")
        print("Login...: ", chave)
        print("Dados...: ", valor)
