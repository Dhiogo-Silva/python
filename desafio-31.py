viagem = float(input('Digite quantos km de viagem: '))
if viagem <= 200:
  valor = (viagem *.50)
  print('O valor da viagem e {}'.format(valor))
else:
 valor2=(viagem *.45)
 print('O valor da viagem e {:.1f}'.format(valor2))
