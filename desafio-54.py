from datetime import date
sim = 0
nao = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input('Em que ano voce nasceu: '))
    idade = atual - ano
    if idade > 18:
      sim += 1
    elif idade < 18:
      nao += 1
print ('{} Ja atigiram a maioridade'.format(sim))
print('{} ainda nao atingiram a maioridade'.format(nao))
print(idade)