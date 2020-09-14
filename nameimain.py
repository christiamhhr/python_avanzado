def main():
	print("Nombre de modulo: ",__name__)
	print("Se ha ejecutado el if.")

if __name__ == "__main__":
	main()
else:
	print("Ejecutandose desde el modulo B")