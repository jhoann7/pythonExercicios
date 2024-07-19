num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')

print('[1] convertar para binário')
print('[2] converter para octal')
print('[3] converter para hexadecimal')

esc = int(input('Sua opção: '))

if esc == 1:
    print('{} convertido para binário é igual {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para octal é igual {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para hexadecimal é igual {}'.format(num, hex(num)[2:]))
else:
    print('{} não é uma opção!')

