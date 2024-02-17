casa = int(input('Qual o valor da casa que deseja comprar: '))
salario =int(input('Qual o seu salario: '))
anos = int(input('Em quantos anos voce quer pagar: '))
parcela = (30*salario)/100
anos2 = anos*12
quantos = (casa/anos2)
if quantos > parcela:
  print('Emprestimo negado !!!')
else:
  print('Emprestimo aprovado !, Com parcelar de {:.2f} em {}'.format(quantos, anos))
print('aa',quantos, parcela)