try:
	with open('texto.txt', 'r', encoding="utf-8") as texto:
		lectura = texto.readlines() #una forma
		#####otra forma de leer
		# for linea in texto:
		# 	print(linea)

	print(lectura)
except FileNotFoundError:
	print("El archivo no se ha encontrado")