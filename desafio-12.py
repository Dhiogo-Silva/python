km = float(input('Quantos km voce rodou? '))
dias = int(input('quantos dias voce alugou o carro? '))
conta = (dias * 60) + (km * 0.15)
 
print ('o total a se pagar e R${}'.format(conta))