
for num in range(1,256):
    print '%3d   %3o   %3x' % (num,num,num)
print '\n'

nombres=['juan','ana','luis']
sueldos=[1500.55,2700.00,910.66]


for indice in range(0,len(nombres)):
    print '%-20s  %10.2f' % (nombres[indice],sueldos[indice])

