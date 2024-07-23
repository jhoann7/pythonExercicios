print(9 * '=-')
print('TERMOS DE UMA PA')
print(9 * '=-')

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dt = pt + (10 - 1) * r
for c in range(pt, dt + 1, r):
    print(c, end=' -> ')
print('Acabou')