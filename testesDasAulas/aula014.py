'''c = 1
while c < 10:
    print(c)
    c = c+1
print('FIM')'''

'''l = 'S'
while l == 'S':
    valor = int(input('Digite um valor: '))
    l = str(input('Quer continuar? ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} n° pares e {} n° ímpares'.format(par, impar))