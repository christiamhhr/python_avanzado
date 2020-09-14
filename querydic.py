from operator import itemgetter

usuarios=[{'id':1,'Nombre':'Enrique','Apellidos':'Barros Fernandez','Edad':28},
		  {'id':2,'Nombre':'Alba','Apellidos':'Molina Santos','Edad':36},
		  {'id':3,'Nombre':'Pepe','Apellidos':'Diaz Garcia','Edad':43},
		  {'id':4,'Nombre':'Maria','Apellidos':'Pons Anglada','Edad':29}
			]
ordenar_id = itemgetter('id')
ordenar_nombre = itemgetter('Nombre')
ordenar_apellidos = itemgetter('Apellidos')
ordenar_edad = itemgetter('Edad')

usuarios.sort(key=ordenar_edad)  #por el campo que quieras ordenar
usuarios.reverse()  #en orden desesndente

for y in usuarios:

	print(y)

#####################forma mas corta#######################
usuarios = sorted(usuarios,key=lambda x: x['Edad'])
for y in usuarios:
	print(y)