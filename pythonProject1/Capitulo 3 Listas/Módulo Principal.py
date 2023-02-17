from Capitulo3_Funções.IdentificaçãoDeFunções import *

minhaLista = []
print("Preenchendo...")
preencherInventario(minhaLista)
print("Exibindo!")
exibirInventario(minhaLista)

print("Pesquisando...")
buscarPorNome(minhaLista)
print("Alternando...")
depreciarPorNome(minhaLista)

print("Excluindo...")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo...")
resumirValores(minhaLista)