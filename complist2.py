a = [sorted(x) for x in [[2,10,0,9,1,3,4,5,8,6,7]]] #asendente
print(a)
a = [sorted(x,reverse=True) for x in [[2,10,0,9,1,3,4,5,8,6,7]]] #asendente
print(a)

############ ordenar
a = [[50,34],[500,2,65],[76,80],[13],[55]]

b = sum(a,[])  #lo junta en n una sola lista

c = sorted(b) #ordena

print(c)

#########ram=ndom
from random import randrange

a = [randrange(1,10000) for x in range(15)]
print(a)

#########################
a = [x for x in range(25) if x % 2 == 0]
print(a)

#####################

a = [x if x % 2 == 0 else "Descartado" for x in range(10)]
print(a)
