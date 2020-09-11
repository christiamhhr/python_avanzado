# exepciones controladas
from collections import defaultdict
def valor_defecto():
	return "Este elemento no existe en el diccionario."

usuario = defaultdict(valor_defecto)

usuario["ID"] = 1
usuario["Nombre"] = "Christiam"
usuario["Apellidos"] = "Hinostroza Robles"
usuario["Edad"] = 30

# usuario = {
# 	"ID" : 1,
# 	"Nombre" : "Christiam",
# 	"Apellidos" : "Hinostroza Robles",
# 	"Edad" : 30
# }

print(usuario["ID"])
print(usuario["Nombre"])
print(usuario["Apellidos"])
print(usuario["Edad"])
print(usuario["Direccion"])
print(type(usuario))