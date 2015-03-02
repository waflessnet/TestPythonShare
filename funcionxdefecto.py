def mostrartitulo(dato,colorletra='#000',colorfondo='#fff'):
    print '<h1 style="color:'+colorletra+';background-color:'+colorfondo+'">'+dato+'</h1>'

mostrartitulo('Primer titulo')
mostrartitulo('Segundo titulo','#f00')
mostrartitulo('Tercer titulo','#f00','#000')

def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s

print sumar(5,6)
print '\n'
print sumar(1,2,3)
print '\n'
x=sumar(1,2,3,4,5)
print x
