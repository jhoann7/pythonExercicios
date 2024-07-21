n1 = float(input('Digite a nota da nap 1: '))
n2 = float(input('Agora a nota da nap 2: '))

media = (n1 + n2) / 2

print('Sua média foi {}'.format(media))

if media < 5:
    print('REPROVADO!')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('Parabéns, você foi APROVADO!')