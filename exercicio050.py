s = 0
for n in range(1, 7):
    
    num = int(input('Digite {}° número: '.format(n)))
    
    if num % 2 == 0:
        s = s + num
print('A soma de todos os números pares é igual a {}'.format(s))
