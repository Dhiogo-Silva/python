preco = float(input('Qual o valor das compras R$: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao ''')
opcao = int(input('Escolha uma das Opcoes: '))
if opcao == 1:
  total = preco - (preco * 10 /100)
elif opcao == 2:
  total = preco -(preco*5/100)
elif opcao == 3:
  total = preco
  totalparc = preco/2
  print('Sua compra de R${} parcela em 2x de {} SEM JUROS'.format(preco, totalparc))
elif opcao == 4:
  total = preco + (preco*20/100)
  quantasparc = input('em quantas parcelas?')
  print('Sua compra de R${} em {} parcelas COM JUROS, vai ficar {}'.format(preco, quantasparc, total))
else:
  total = preco
  print('OPCAO INVALIDA')
print('Sua compra de R${}, vai ficar R${}'.format(preco, total))