print('----- GERADOR DE PA -----')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer usar a mais? '))
print('Operação finalizada com {} termos mostrados'.format(total))