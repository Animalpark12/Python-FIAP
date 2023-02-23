from ftplib import *
ftpAtivo = False  # False representa uma conexão passiva (requer menos segurança, mais comum)
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario = input("Digite o usuário: ")
senha = input("Digite a sua senha: ")
ftp.login(usuario, senha)

print("Diretório atual de trabalho: ", ftp.pwd())  # PWD retorna o endereço atual de trabalho
ftp.cwd('pub')  # Navegar entre os diretórios
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()