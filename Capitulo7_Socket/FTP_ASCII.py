import os
from ftplib import *


def escreverLinha(data):
    arq.write(data)  # Recebera o conteudo da linha
    arq.write(os.linesep)  # Irá separar a linha


ftpAtivo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
arquivo = 'LEIAME'
ftp.set_pasv(ftpAtivo)
with open(arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escreverLinha)
    # 1° argumento é o retorno (RETR) + nome do arquivo
    # 2° função criada para escrever
ftp.quit()
