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

for equipamento in equipamentos:
    print("Equipamento: ", equipamento)