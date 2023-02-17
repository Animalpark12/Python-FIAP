def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite 'S' para continuar adicionando itens: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Número serial: ", elemento[2])
        print("Departamento.: ", elemento[3])

def buscarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor.............: ", elemento[1])
            print("Número do Serial..: ", elemento[2])
            print("Departamento......: ", elemento[3])

def depreciarPorNome(lista):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] *= 0.9
            print("Novo Valor: ", elemento[1])

def excluirPorSerial(lista):
    serial = int(input("Digite o serial do objeto a ser deletado: "))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos."

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))