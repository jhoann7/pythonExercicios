import random
from time import sleep
n = int(input('Digite um número de 1 a 5: '))
print('PROCESSANDO...')
sleep(3)
comp = random.randint(1, 5)

if n == comp:
    print('Parabéns, você acertou!')
    print('O número é {}'.format(comp))
else:
    print('Você errou!')
    print('O número é {}'.format(comp))