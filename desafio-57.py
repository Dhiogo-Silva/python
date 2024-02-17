
sexo =str(input('Qual seu sexo? [M/F]')).strip().upper()[0]

while sexo != 'M' and sexo != 'F': # while sexo not in 'MnFf
      print('Voce digitou errado! tente novamente!')
      sexo =str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
      

print('fim')
