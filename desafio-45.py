import random
print('-=' *11)
print('''BEM-VINDO''')
print('-=' *11)
nome = input('Qual seu nome de jogador? ')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint (0, 2)
print ('''SUAS OPCOES
       [ 0 ] PEDRA 
       [ 1 ] PAPEL
       [ 2 ] TESOURA''')
jogador = int(input('Escolha sua jogada: '))
print('-=' *11)
print('Computador jogou {}'.format(itens[computador]))
print('{} jogou {}'.format(nome ,itens[jogador]))
print('-=' *11)

if computador == 0 :
       if jogador == 0:
            print('EMPATE')

       elif jogador == 1:
            print('{} Venceu'.format(nome))

       elif jogador == 2:
            print('Computador vence')
       
       else:
            print('Jogada INVALIDA')

elif computador == 1 :

       if jogador == 0:
              print('{} Venceu'.format(nome))
       
       elif jogador == 1:
              print('EMPATE')
              
       
       elif jogador == 2:
              print('Computador vence')
       
       else:
              print('Jogada INVALIDA')

elif computador == 2 :
       if jogador == 0:
              print('{} Venceu'.format(nome))
       elif jogador == 1:
             print('Computador vence')

       elif jogador == 2:
             print('EMPATE')
       else:
             print('Jogada INVALIDA')

    




    