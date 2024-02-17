peso = int(input('Qual e o seu peso atual: '))
altura = float(input('Qual sua altura: '))
imc = peso/(altura*altura)
if imc < 18.5:
  print('Voce esta abaixo do peso')
elif imc > 18.5 and imc<25.0: # 18.5 <= imc <25
  print('Peso ideal')
elif imc >25.0 and imc <30.0:
  print('Sobrepeso')
elif imc >30.0 and imc<40.0:
  print('OBESO')
elif imc >40.0:
  print('GORDO DEMAIS')
print('seu calculo imc e {:.1f}'.format(imc))