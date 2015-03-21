import random
x=random.randint(1,100)
y=random.randint(1,100)

class Operacion:
    def cargar1(self,v1):
        self.valor1=v1
    def cargar2(self,v2):
        self.valor2=v2
    def imprimir(self):
        print self.resultado
        print '\n'


class Suma(Operacion):
    def operar(self):
        self.resultado=self.valor1+self.valor2


class Resta(Operacion):
    def operar(self):
        self.resultado=self.valor1-self.valor2

class Multiplicacion(Operacion):
    def operar(self):
        self.resultado=self.valor1*self.valor2

class Division(Operacion):
    def operar(self):
        self.resultado=self.valor1/self.valor2

print x,' ',y


s=Suma()
s.cargar1(x)
s.cargar2(y)
s.operar()
print 'La suma es:'
s.imprimir()
r=Resta()
r.cargar1(x)
r.cargar2(y)
r.operar()
print 'La resta es:'
r.imprimir()
m=Multiplicacion()
m.cargar1(x)
m.cargar2(y)
m.operar()
print 'La Multiplicacion es:'
m.imprimir()
d=Division()
d.cargar1(x)
d.cargar2(y)
d.operar()
print 'La Division es:'
d.imprimir()
