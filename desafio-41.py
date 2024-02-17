from datetime import date
atual = date.today().year
ano= int(input('Digite o ano em que voce nasceu : '))
idade = atual-ano
if idade <= 9:
  print('Sua categoria e  MIRIM')
elif idade <= 14:
  print('Sua categoria e INFANTIL')
elif idade <= 19:
  print('Sua categoria e JUNIOR')
elif idade <= 25:
  print('Sua categoria e Senior')
else:
  print('Sua categoria e MASTER')