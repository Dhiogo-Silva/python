for c in range(0, 5):
  print('dhiogo')
for c in range(6, 0, -1):
  print(c)

n = int(input('Digite um numero: '))
for c in range(0, n+1):
  print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p)  #f+1 = o numero final vai ser o que foi digitado, sem ele fica com menos um
  print(c)

s = 0
for c in range(0, 4):
  n = int(input('Digite um numero: '))
  s += n
print(s)