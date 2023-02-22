from socket import *

servidor = "127.0.0.1"  # O número é para indicar um servidor da própria máquina (local host)
porta = 43210  # Pode ser qualquer número de porta de 0 a 65535
objSocket = socket(AF_INET, SOCK_STREAM)
# O primeiro é responsavel por identificar pacote (identificação do emissor/receptor dos pacotes via DNS ou número IP)
# O segundo é o transporte do pacote (protocolo TCP)
objSocket.bind((servidor, porta))  # Associação com o servidor e a porta
objSocket.listen(2)  # Número máximo de clientes
print("Aguardando cliente....")
while True:  # Aguarda a chamada de um cliente
    con, cliente = objSocket.accept()  # Recebe uma tupla e coloca no cliente, con é a identificação
    print("Conectado com: ", cliente)
    while True:  # Envia solicitação q pode ser transmitida até 1024 bytes
        msgRecebida = str(con.recv(1024))
        print("Recebemos: ", str(msgRecebida)[2:-1])
        msgEnviada = bytes(input("Sua resposta: "), 'utf-8')
        con.send(msgEnviada)
        break
    con.close()
