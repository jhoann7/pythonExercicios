from random import randint
v = 0
while True:
    num = int(input('Digite um número: '))
    comp = randint(0, 10)
    total = num + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {num} e o computador jogou {comp}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            print('Vamos jogar novamente? ')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            print('Vamos jogar novamente? ')
            v +=1
        else:
            print('Você perdeu!')
            break
print(f'Game Over, você venceu {v} vezes!')

