equipamentos = []
valor = []
numeroSerial = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Digite o nome do equipamento: "))
    valor.append(float(input("Digite o valor: ")))
    numeroSerial.append(int(input("Digite o número serial: ")))
    departamento.append(input("Digite o nome do departamento: "))
    resposta = input("Para continuar, digite 'S': ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento.......: ", (indice + 1))
    print("Nome..............: ", equipamentos[indice])
    print("Valor.............: ", valor[indice])
    print("Número do Serial..: ", numeroSerial[indice])
    print("Departamento......: ", departamento[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor.............: ", valor[indice])
        print("Número do Serial..: ", numeroSerial[indice])
        print("Departamento......: ", departamento[indice])

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valor[indice])
        valor[indice] *= 0.9
        print("Novo Valor: ", valor[indice])

danificado = int(input("Digite o serial do equipamento que será descartado: "))
for indice in range(0, len(equipamentos)):
    if danificado == numeroSerial[indice]:
        del equipamentos[indice]
        del valor[indice]
        del numeroSerial[indice]
        del departamento[indice]
        break
for indice in range(0, len(equipamentos)):
    print("Equipamento.......: ", (indice + 1))
    print("Nome..............: ", equipamentos[indice])
    print("Valor.............: ", valor[indice])
    print("Número do Serial..: ", numeroSerial[indice])
    print("Departamento......: ", departamento[indice])