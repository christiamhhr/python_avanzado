a = 10
print(type(a))

a = 10.55
print(type(a))

a= "Programacion Facil"
print(type(a))

a = True
print(type(a))

a = None
print(type(a))

#pruebas
a = False 
if (a is True):
	pritn("verdadera")
else:
	print("falsa")

# ?convertir tipos de datos 

a = "10"

a = int(a)
print(type(a))

a= "10.234"
a = float(a)
print(type(a))

# conversion de listas y tuplas 

a = "Programacion Fácil"
b = list(a) #lista
b = set(a) #set
print(b,type(b))
