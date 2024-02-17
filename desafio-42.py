r1 = int(input('Insira o valor da reta 1: ') )
r2 = int(input('Insira o valor da reta 2: ') )
r3 = int(input('Insira o valor da reta 3: ') )
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
  print('eles podem formar um triangulo')
elif r1 == r2 == r3:
  print('Voce tem um triangulo EQUILATERO')
  print('Voce tem um triangulo ISOCELES')
elif r1 != r2 != r3 != r1 :
  print('Voce tem um triangulo ESCALEANO')
else:
  print('ISOSELES')
  print('Nao podem formar um triangulo')