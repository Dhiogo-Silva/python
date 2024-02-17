n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if n1 > n2:
  print('O {} e o valor maior'.format(n1))
elif n2 > n1:
  print('O {} e o valor maior'.format(n2))
else:
  print('Nao existe valor maior os dois sao iguais')