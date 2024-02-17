n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
  if n % c == 0  :
    tot += 1
  
if tot == 2:
  print('E um numero primo')
else:
    print('Nao e primo')