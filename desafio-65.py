r = 'S'
maior = 0
menor = 0
soma = 0
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]')).upper()
    if r =='S':
        soma += n
        maior = n
        menor = n
    if n > maior :
        maior = n
    if n < menor:
        menor = n
    if r == 'N':
        media = soma / 4
print('A media dos numeros {}'.format(media))
print('E o numero maior foi {}, e o menor foi {}'.format(maior, menor))