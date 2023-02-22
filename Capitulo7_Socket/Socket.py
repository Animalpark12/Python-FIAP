import socket

resposta = "S"
while resposta == "S":
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referente a URL é: ", ip)
    resposta = input("Digite <S> para continuar: ").upper()