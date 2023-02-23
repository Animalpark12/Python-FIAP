from ftplib import *
ftpAtivo = False  # False representa uma conexão passiva (requer menos segurança, mais comum)
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario = input("Digite o usuário: ")
senha = input("Digite a sua senha: ")
ftp.login(usuario, senha)

resposta = "S"
while resposta == "S":
    print("Diretório atual de trabalho: ", ftp.pwd())  # PWD retorna o endereço atual de trabalho
    print(ftp.retrlines('LIST'))
    ftp.cwd(input("Digite o diretório que deseja entrar: "))  # Navegar entre os diretórios
    print("Diretório corrente: ", ftp.pwd())
    resposta = input("Para continuar, digite <S>: ").upper()
ftp.quit()