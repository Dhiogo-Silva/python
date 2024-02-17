salario = float(input('Digte seu valor salarial:R$'))
a2 = 15/100
if salario >= 1.250:
   novoSalario = salario * 1.10
   print('Seu novo salario com 10 porcento de aumento e {:.3f}'.format(novoSalario))
else:
   novoSalario2= salario * 1.15
   print('Seu novo salario com 15 porcento de aumento e {:.3f}'.format(novoSalario2))