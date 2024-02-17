num = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases de cornversao:
            [1] Binario
            [2]Octal 
            [3]Hexadecimal ''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
  print('{} convertido para Binario e {}'.format(num, bin(num)[2:]))
elif opcao == 2:
  print('{} convertido para Octal e {}'.format(num, oct(num)[2:]))
elif opcao == 3:
  print('{} convertido para Hexadecimal e {}'.format(num, hex(num)[2:]))
else:
  print('Opcao invalida, tente novamente.')