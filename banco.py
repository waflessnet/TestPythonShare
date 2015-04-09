class Cliente:
    def __init__(self,nom,mon):
        self.nombre=nom
        self.monto=mon
    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1200)
cli2=Cliente('Luis',1500)
print 'El total depositado es '
print cli1+cli2
