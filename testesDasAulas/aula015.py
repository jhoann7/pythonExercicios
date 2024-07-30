'''cont = 1
while cont <= 10:
    print (cont, ' ', end='')
    cont += 1'''

'''cont = 1
while True:
    print (cont, ' ', end='')
    cont += 1'''

'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

'''n = 'José'
id = 33

print(f'O {n} tem {id} anos.')
print('O {} tem {} anos.'.format(n, id))
print('O %s tem %d anos.' % (n, id))'''

nome = 'José'
idade = 33
salário = 1500.0

print(f'O {nome} tem {idade} anos e recebe R${salário:.2f}')