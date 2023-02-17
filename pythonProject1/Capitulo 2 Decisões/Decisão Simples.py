nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
prioridade = "não ";

if idade >= 65:
    prioridade = ""

print("O paciente é " + nome + " possui " + str(idade) + " e por isso " + prioridade + "possui prioridade!")