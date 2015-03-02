personas=[('juan',22),('ana',40),('carlos',15)]

may=-1
for nombre,edad in personas:
    if edad>may:
        nom=nombre
        may=edad
print '%s tiene la edad mayor y es de %d' % (nom,may)