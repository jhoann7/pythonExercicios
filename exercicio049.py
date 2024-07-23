num = int(input('Digite um número para ver sua tabuada: '))
for n in range(1, 11):
    
    tot = num * n
    print('{} x {:2} = {}'.format(num, n, tot))