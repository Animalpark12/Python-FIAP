inventario = []
resposta = "S"
#Armazena o que tem na lista
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

#Mostra o que tem na lista
for elemento in inventario:
    print(elemento)