#para buscar una palabra en un archivo externo

import re
try:
	palabra = "poesias"
	with open('texto.txt', 'r', encoding="utf-8") as texto:
		###para buscar algo especifico en el archivo
		for x in texto:
			buscar = re.search(palabra,x)
			
		if buscar:
			print('La palabra', palabra, "ha sido encontrada")
		else:
			print('no se encontro ', palabra)

except FileNotFoundError:
	print("El archivo no se ha encontrado")