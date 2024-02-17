frase = str(input('Digite um frase qualuquer: ')).strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] 
print(inverso)
if inverso == junto:
    print('e um palindromo')
else:
    print('nao e um palindromo')