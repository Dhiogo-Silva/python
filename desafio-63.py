n = int(input('Digite um numero: '))
s = 0
fibo = 0

while s > n:
  fibo += 1
  s += fibo
  fibo += s
      
print('{} x  {} '.format(s, fibo))


