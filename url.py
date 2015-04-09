class URL:
    def __init__(self,dir,men):
        self.direccion=dir
        self.mensaje=men
    def __str__(self):
        cadena='<a href="%s">%s</a>' % (self.direccion,self.mensaje)
        return cadena

url1=URL('http://www.google.com.ar','Google')
url2=URL('http://www.yahoo.com.ar','Yahoo')
url3=URL('http://www.live.com','Live')
print url1
print url2
print url3
