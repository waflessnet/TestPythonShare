
class MyClass:
    i = 12345
    def f(self):
        return "hello world \n"
    def d(self,argumento):
	print 'tu puto arg: %s'%argumento

#llamar la clase
x = MyClass()
print x.f()
x.d('chupalo')
print '\n'


class Persona:
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print 'Nombre:'
        print self.nombre
        print '\n'

persona1=Persona()
persona1.inicializar('Juan')
persona1.imprimir()

persona2=Persona()
persona2.inicializar('Ana')
persona2.imprimir()


print '\n'


class Empleado:
    def inicializar(self,nom,suel):
        self.nombre=nom
        self.sueldo=suel
  
    def pagaimpuestos(self):
        print 'Nombre:'
        print self.nombre
        print '\n'
        print 'Sueldo:'
        print self.sueldo
        print '\n'
        if self.sueldo>300:
            print 'Debe pagar impuestos'


emp1=Empleado()
emp1.inicializar('Juan',3500)
emp1.pagaimpuestos()



















