from geopy.geocoders import Nominatim
from Funcoes.Funcoes_JSON import lerArquivo, gravarArquivo

geolocator = Nominatim(user_agent="wazeyes")
dicionario = lerArquivo("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida = {"coordenadas": (location.latitude, location.longitude)}
gravarArquivo(saida, "saida.json")
