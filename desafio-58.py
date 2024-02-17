import random

tentativas = 1

numero = random.randint(0, 10)
chute = int(input('Digite um numero de 0 ate 10: '))

while chute != numero:
     print('Voce errou!')
     tentativas += 1
     chute = int(input('Digite um numero de 0 ate 10: '))
     if chute == numero:
          print('Voce acertou')
print('O numero certo e {}'.format(numero))
print('Voce acertou com {} tentativas'.format(tentativas))