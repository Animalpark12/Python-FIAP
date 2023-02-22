from socket import *

servidor = "127.0.0.1"
porta = 43210

objSocket = socket(AF_INET, SOCK_DGRAM)
objSocket.connect((servidor, porta))
saida = ""
while saida != "X":
    msg = input("Sua mensagem: ")
    objSocket.sendto(msg.encode(), (servidor, porta))
    dados, origem = objSocket.recvfrom(65535)
    print("Resposta do servidor: ", dados.decode())
    saida = input("Digite <X> para sair: ").upper()
objSocket.close()