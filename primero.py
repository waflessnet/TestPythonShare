import random

x=random.randint(1,20)
y=random.randint(1,20)
z=random.randint(1,20)
print '1r valor: ',x 

print '2o valor: ',y 

print '3r valor: ',z


def sumarmayores(x,y,z):
	if x>=y and x>=z:
		if y>=z:
			return x+y
		else:
			return x+z

	elif y>=x and y>=z:
		if x>=z:
			return y+x
		else:
			return y+z

	elif z>=x and z>=y:
		if x>=y:
			return z+x
		else:
			return z+y

suma=sumarmayores(x,y,z)

print 'la suma de los valores mayores es ',suma

		


