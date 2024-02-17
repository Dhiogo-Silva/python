m1 = float(input('Digite a primeira nota: '))
m2 =float(input('Digite a segunda nota: '))
media =(m1+m2)/2
if media >= 7.0:
  print('Voce esta APROVADO')
elif media < 5.0:
  print('Voce esta REPROVADO')
elif media == 5.0 and media < 7: #ou if 7 > media >=5
  print('Voce esta de RECUPERACAO')
