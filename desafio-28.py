import random
numero = random.randint(0, 5)
chute = int(input('Digite um numero de 0 ate 5: '))
if chute == numero:
  print('Voce acertou')
else:
  print('Voce errou')
print('O numero certo e {}'.format(numero))