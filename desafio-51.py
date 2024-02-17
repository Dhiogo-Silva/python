r = int(input('Digite a razao: '))
pt = int(input('Digite o primeiro termo da PA: '))
decimo = pt + (10-1) * r

for c in range(pt, decimo+ r ,r):
  print(c)