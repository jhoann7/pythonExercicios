num = int(input('Me diga um número qualquer: '))
n = num % 2
if n == 0:
    print('{} é um número par!'.format(num))
else:
    print('{} é um número ímpar!'.format(num))