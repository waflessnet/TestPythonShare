#meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
#cantidaddias=(31,28,31,30,31,30,31,31,30,31,30,31)
#indice=0
#while indice<len(meses):
#    print meses[indice],':',cantidaddias[indice]
#    print '\n'
#    indice=indice+1

#Definir una tupla que almacene 5 enteros. Implementar un algoritmo que imprima la suma de todos los elementos.
numeros=(1,2,3,4,5)
suma=0
indice=0
while indice<len(numeros):
	print 'la suma de',suma,' + ',numeros[indice],'es:'
	suma=suma+numeros[indice]
	print suma,'\n'
	indice=indice+1