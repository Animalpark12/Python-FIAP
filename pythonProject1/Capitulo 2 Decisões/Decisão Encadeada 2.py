nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doencaContagiosa = input("Suspeita de doença infecto-contagiosa?: ").upper()

#RESOLVER A SALA
if doencaContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif doencaContagiosa == "NAO":
    print("Encaminhe o paciente para a sala BRANCA")
else:
    print("Por favor, resposta a pergunta com 'sim' ou 'nao'.")

#RESOLVER O GENERO E GRAVIDEZ
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida?: ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")