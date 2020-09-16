potencias = [x*x for x in (1,2,5,10,50)]
print(potencias)

######## otra forma
potencias2=[]
for x in (1,2,5,10,50):
	x *= x
	potencias2.append(x)

print(potencias2)

####### upper and lower, capitalize

colores = ["rojo","azul","verde","amarillo"]

colores_mayus = [x.upper() for x in colores]

print(colores_mayus)

#########otro ejemplo elimnar caracteres(.)
l1=[x.strip(".") for x in ["Esto.","es","un","texto.","en","varios.","strings"]]
print(l1)

###mas ejemplos con if y else
l1 = [x if x in 'pny' else 'Caracter no encontrado' for x in 'python']
print(l1)

###### la forma convencional
l2 =[]

palabra = 'python'
for x in palabra:
	if x in 'pny':
		l2.append(x)
	else:
		l2.append('Caracter no encontrado')

print(l2)