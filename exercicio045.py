from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Escolha uma opção: '))

if jogador >= 0 and jogador < 3:
    print(40 * '=')
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print(40 * '=')
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR GANHOU')
        elif jogador == 2:
            print('COMPUTADOR GANHOU')
        elif jogador > 2 and jogador < 0:
            print('JOGADA INVÁLIDA')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR GANHOU')
        elif jogador > 2 and jogador < 0:
            print('JOGADA INVÁLIDA')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR GANHOU')
        elif jogador == 1:
            print('COMPUTADOR GANHOU')
        elif jogador == 2:
            print('EMPATE')
        elif jogador > 2 and jogador < 0:
            print('JOGADA INVÁLIDA')
else:
    print('Jogada inválida')

