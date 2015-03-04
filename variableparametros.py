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