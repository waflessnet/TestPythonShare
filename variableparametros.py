def sumar(x1,x2,*xn):
    s=x1+x2
    for valor in xn:
        s=s+valor
    return s

print sumar(1,2)
print '\n'
print sumar(1,2,3,4)
print '\n'
print sumar(1,2,3,4,5,6,7,8,9,10)


def cantidadmayor18(ed1,*edades):
    cant=0
    if ed1>18:
        cant=cant+1
    for e in edades:
        if e>18:
            cant=cant+1
    return cant


print 'Cantidad de personas mayores a 18:'
cant=cantidadmayor18(4,56,14,67,32,21)
print cant