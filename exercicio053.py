frase = str(input('Digite a frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''

# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')