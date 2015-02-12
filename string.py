#ejercicio string

def primercaracter(cadena):
    return cadena[0]

def concatenar(apellido,nombre):
    return apellido+','+nombre

def menor(cadena1,cadena2):
    if len(cadena1)<len(cadena2):
        return cadena1
    else:
        return cadena2


cad='Hola Mundo'
print 'Primer caracter de '+cad+' es '+primercaracter(cad)
print '\n'
nom='juan'
ape='rodriguez'
print 'Apellido y nombre concatenados:'+concatenar(ape,nom)
cad1='Hola'
cad2='Fin'
print '\n'
print 'De: '+cad1+' y '+cad2+' tiene menos caracteres '+menor(cad1,cad2)



 #ejercicio string lista

 nombres=['ariel','marcos','ana','luis','pedro','andres']
cant=0
for nom in nombres:
    if nom[0]=='a':
        cant=cant+1
print nombres
print '\n'
print 'Cantidad de nombres que comienzan con a es:'
print cant
    