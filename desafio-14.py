import math
cateto = int(input('Insira o cateto oposto: '))
adjacente = int(input('Insira o cateto adjacente: '))
hipotenusa = (cateto*cateto)+(adjacente*adjacente)
raiz = math.sqrt(hipotenusa)

print('o comprimento da hipotenusa e {}'.format(raiz))