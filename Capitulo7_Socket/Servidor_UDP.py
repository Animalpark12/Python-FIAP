from socket import *

servidor = "127.0.0.1"
porta = 43210

objSocket = socket(AF_INET, SOCK_DGRAM)  # protocolo UDP
objSocket.bind((servidor, porta))
print("Servidor pronto...")
while True:
    dados, origem = objSocket.recvfrom(65535)  # recvfrom não possui ligação com o objeto de conexão
    print("Origem...........: ", origem)
    print("Dados recebidos..: ", dados.decode())
    resposta = input("Digite a sua resposta: ")
    objSocket.sendto(resposta.encode(), origem)
objSocket.close()