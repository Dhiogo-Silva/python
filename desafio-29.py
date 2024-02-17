velocidade = int(input('Digite a velocidade do carro: '))
if velocidade >= 80:
  print('Voce foi multado')
  multa = (velocidade-80)*7
  print('O valor da multa foi {}'.format(multa))