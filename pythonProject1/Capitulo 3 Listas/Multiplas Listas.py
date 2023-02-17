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
    print("Valor.............: ", str(valor[indice]))
    print("Número do Serial..: ", numeroSerial[indice])
    print("Departamento......: ", departamento[indice])