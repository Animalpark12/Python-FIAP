nivelDeAcesso = input("Digite o seu nível de acesso: ").upper()

if nivelDeAcesso == "ADM" or nivelDeAcesso == "USR":
    genero = input("Digite o seu gênero: ").upper()
    if nivelDeAcesso == "ADM":
        if genero == "FEMININO":
            print("Olá administradora!")
        else:
            print("Olá administrador!")
    else:
        if genero == "FEMININO":
            print("Olá usuária!")
        else:
            print("Olá usuário!")
elif nivelDeAcesso == "GUEST":
    print("Olá visitante!")
else:
    print("Por favor, responda com 'Adm', 'Usr' ou 'Guest'")