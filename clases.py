
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
