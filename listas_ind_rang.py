a = [1,2,3]
a.extend(range(4,10))
print(a)

# concatenar listas
a = [1,2,3]
b = [7,8,9]
c = a+ [4,5,6] + b
print(c)

# posiciones
a = []
a.extend(range(3000,10000))
indice =  a.index(9000)
print(indice)