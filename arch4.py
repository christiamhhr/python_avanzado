#######reading mode plus r+ para abrir y escribir al  mismo tiempo 
### para que cree si no existe el archivo poner w+ es similar el a+
try:
	with open('texto2.txt','r+',encoding="utf-8") as texto:
		for linea in texto:
			print(linea)
		texto.write("\nEesta es otra linea con r+.")
		print("Se aniadio el contenido al final de archivo")


except FileNotFoundError:
	print("El archivo no existe.")
