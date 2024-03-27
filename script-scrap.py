import re
from colorama import Fore
import requests

maquinas_inicial = []
with open("maquinas_inicial.txt", "r") as file:
    maquinas_inicial = [maquina.rstrip() for maquina in file]

# website = "https://vulnhub.com/"
website = "https://vulnhub.com/?page=2"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, str(content))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []
for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)

color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW

if sorted(maquinas_inicial) == sorted(maquinas_final):
    print(color_verde + "no hay maquina nueva")
else:
    print(color_amarillo + "maquina nueva")
    with open("maquina anterior.txt", 'w') as file:
        list(map(lambda maquina: file.write(maquina + '\n'), maquinas_inicial))
    with open("maquinas_inicial.txt", 'w') as file:
        list(map(lambda maquina: file.write(maquina + '\n'), maquinas_final))
