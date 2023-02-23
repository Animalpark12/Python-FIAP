import serial

conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 9600, timeout=0.5)
        #  1° argumento: representar a saida serial
        #  2° argumento: capacidade de transmissão de bit por segundo (o mesmo número tem q estar no arduino)
        #  3° argumento: tempo que ira demorar para colher as informações
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    conexao.close()
    print("Conexão encerrada!")
else:
    print("Sem portas disponíveis.")