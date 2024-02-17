from datetime import date
atual = date.today().year
ano = int(input('Em que ano voce nasceu: '))
idade = atual - ano
if idade == 18:
  print('Esta na hora de se alistar!')
elif idade < 18:
  print('Voce ainda vai se alistar!')
  tempo = (18-idade)
  print('Ainda falta {} anos para voce se alistar'.format(tempo))
else:
  print('JA PASSOU DA HORA DE SE ALISTAR !!!')
  tempo2 = (idade-18)
  print('Voce atrasou seu alistamento em {} anos'.format(tempo2))