nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doencaContagiosa = input("Suspeita de doença infecto-contagiosa?: ").upper()

if idade >= 65 and doencaContagiosa == "SIM":
    print("O paciente será direcionado para a sala Amarela - COM prioridade!")
elif idade < 65 and doencaContagiosa == "SIM":
    print("O paciente será direcionado para a sala Amarela - SEM prioridade!")
elif idade >= 65 and doencaContagiosa == "NAO":
    print("O paciente será direcionado para a sala Branca - COM prioridade!")
elif idade < 65 and doencaContagiosa == "NAO":
    print("O paciente será direcionado para a sala Branca - SEM prioridade!")
else:
    print("Responda se possui doença com sim ou não!")