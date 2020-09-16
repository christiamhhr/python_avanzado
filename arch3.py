try:
	with open('texto2.txt','a',encoding="utf-8") as texto:
		texto.write("\nEsta es la tercera linea.")
		print ("Se aniadio este texto")


except FileNotFoundError:
	print("El archivo no existe.")