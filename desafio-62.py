n =1 
s =0
d = 0
while d != 999:
  d = int(input('Digite um numero: '))
  if d != 999:
    s +=d
  else:
    print('fim')
print('A soma e {}'.format(s))