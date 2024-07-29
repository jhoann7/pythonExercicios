num = 0
total = 0
cont = 0
num = int(input('Digite 999 para parar: '))
while num != 999:
    total += num
    cont += 1
    num = int(input('Digite 999 para parar: '))
print('Você digitou {} números e a soma de todos os valores digitados é igual a {}'.format(cont, total))
