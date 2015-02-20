import random

valor=random.randint(1,1000000)
print valor
print '\n'
cadena=str(valor)
indice=-1
iguales=0
for x in range(0,len(cadena)/2):
    if cadena[x]==cadena[indice]:
        iguales=iguales+1
    indice=indice-1
if iguales==(len(cadena)/2):
    print 'Es capicua'
else:
    print 'No es capicua','\n'



lista=['juan','ana','luis','pedro']
print lista
print '\n'
aux=lista[0]
lista[0]=lista[-1]
lista[-1]=aux
print lista