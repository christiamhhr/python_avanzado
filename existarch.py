import os
ruta = os.path.isfile("media/texto.txt")
print(ruta) #es True o  False dependiendo si encuentre o no el archivo

#con un input para la ruta

entrada =  input("Introduce una ruta de archivo:\n")
ruta = os.path.isfile(entrada)
if ruta:
	print('el archio existe')
else:
	print("El archivo no existe")


##### para saber si un directorio existe

entrada =  input("Introduce una ruta:\n")

if os.path.exists(entrada):
	print('La ruta existe')
else:
	print("La ruta no existe")
