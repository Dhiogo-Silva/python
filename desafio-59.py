valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

print('''
        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]novos numeros
        [5]sair do progama
''')

opcoes = int(input('Escolha uma das opcoes acima: '))

while opcoes != 5:
  if opcoes == 1:
      soma = valor1 + valor2
      print('A soma dos valores e {}'.format(soma))
      opcoes = int(input('Se desejar continuar, Escolha uma das opcoes acima: '))     
  if opcoes == 2:
     multi = valor1 * valor2
     print('A multiplicacao dos valores e {}'.format(multi))
     opcoes = int(input('Se desejar continuar, Escolha uma das opcoes acima: '))
  if opcoes == 3:
        if  valor1 > valor2:
            maior = valor1
            print('O maior numero e {}'.format(maior))
        if valor2 > valor1:
            maior = valor2
            print('O maior numero e {}'.format(maior))
        opcoes = int(input('Escolha uma das opcoes acima: '))
  if opcoes == 4:
     valor1 = int(input('Digite um valor: '))
     valor2 = int(input('Digite um valor: '))
     print('seus novos numeros sao {} e {}'.format(valor1, valor2))
     opcoes = int(input('Se desejar continuar, Escolha uma das opcoes acima: '))
  if opcoes == 5:
      print('Encerrando programa')