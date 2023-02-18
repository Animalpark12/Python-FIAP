def perguntar():
    resposta = input("O que deseja realizar? \n"
                     +
                     "<I> - Para Inserir/Modificar um equipamento \n"
                     +
                     "<E> - Para Exibir todos os equipamento \n"
                     +
                     "<P> - Para Pesquisar um equipamento \n"
                     +
                     "<D> - Para Deletar um equipamento \n"
                     +
                     "Comando: ").upper()
    return resposta


def preencherDicionario(dicionario):
    resposta = "S"
    while resposta == "S":
        numeroSerial = int(input("Digite o número serial do objeto: "))
        dicionario[numeroSerial] = [input("Equipamento: ").upper(),
                                    float(input("Valor: ")),
                                    input("Departamento: ").upper()]
        resposta = input("Digite <S> para continuar adicionando itens: ")


def pesquisarDicionario(dicionario, numeroSerial):
    lista = dicionario.get(numeroSerial)
    if lista != None:
        print("Equipamento...: ", lista[0])
        print("Valor.........: ", lista[1])
        print("Departamento..: ", lista[2])

def listarDicionario(dicionario):
    for chave, dado in dicionario.items():
        print("\nObjeto abaixo..: ")
        print("Número serial..: ", chave)
        print("Dados..........: ", dado )

def excluir(dicionario, numeroSerial):
    if dicionario.get(numeroSerial) != None:
        del dicionario[numeroSerial]
    print("Objeto deletado com sucesso!")