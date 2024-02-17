
numero =int(input('Digite um numero: '))
c = numero
f = 1
while c > 0:
        f *= c
        c-= 1
print('o fatorial de {} e {} '.format(numero, f))