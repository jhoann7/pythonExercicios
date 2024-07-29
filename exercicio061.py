print('----- GERADOR DE PA -----')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1

while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('Fim')