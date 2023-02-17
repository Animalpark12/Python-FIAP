resposta = "SIM"
while resposta == "SIM":
    nivel = input("Digite um nível de acesso: ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu gênero:").upper()
        if nivel == "ADM":
            if genero == "FEMININNO":
                print("olá administradora!")
            else:
                print("olá administrador!")
        else:
            if genero == "FEMININO":
                print("olá usuária!")
            else:
                print("olá usuário!")
    elif nivel == "GUEST":
        print("olá visitante!")
    else:
        print("olá desconhecido!")
    resposta = input("Digite SIM para continuar: ").upper()