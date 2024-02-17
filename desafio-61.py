r = int(input('Digite a razao: '))
pt = int(input('Digite o primeiro termo da PA: '))
decimo = pt + (10-1) * r
contador = 0

while pt < decimo:
    print(pt)
    pt = pt +r
opcao = str(input('Voce quer mostrar mais algum termo? [S/N]')).upper()
if opcao == 'S':
          quant = int(input('Quantos termos: '))
          novo = decimo +(quant-1)*r
          while pt < novo:
              print(pt)
              pt += r
opcao = str(input('Voce quer mostrar mais algum termo? [S/N]')).upper()
if opcao == 'N':
          print('Fim')
          

    
    
