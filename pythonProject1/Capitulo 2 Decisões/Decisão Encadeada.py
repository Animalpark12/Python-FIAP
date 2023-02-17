nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doencaContagiosa = input("Suspeita de doença infecto-contagiosa?: ").upper()

if idade >= 65:
    print("Paciente COM prioridaed")
    if doencaContagiosa == "SIM":
        print("O paciente deverá ser encaminhado para a sala AMARELA")
    elif doencaContagiosa == "NAO":
        print("O paciente deverá ser encaminhado para a sala BRANCA")
    else:
        print("Por favor, responda a pergunta com 'sim' ou 'não'.")
else:
    print("Paciente SEM prioridade")
    if doencaContagiosa == "SIM":
        print("O paciente deverá ser encaminhado para a sala AMARELA")
    elif doencaContagiosa == "NAO":
        print("O paciente deverá ser encaminhado para a sala BRANCA")
    else:
        print("Por favor, responda a pergunta com 'sim' ou 'não'.")