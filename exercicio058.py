from random import randint
print(''' Sou seu computador...
Acabei de pensar em um número entre 0 e 10!
Será que você consegue adivinhar qual foi?''')
comp = randint(0, 10)
s = ''
tent = 0
while comp != s:
    s = int(input('Qual é o seu palpite? '))
    tent = tent + 1
    if s > comp:
        print('Menos... Tente mais uma vez!')
    elif s < comp:
        print('Mais... Tente mais uma vez!')
print('Acertou com {} tentativas, Parabéns!'.format(tent))