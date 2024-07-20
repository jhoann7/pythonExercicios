ano = int(input('Em qual ano você nasceu? '))
idade = 2024-ano

print('você nasceu em {} e tem {} anos em 2024'.format(ano, idade))

if idade < 18:
        print('Ainda faltam {} anos para o seu alistamento'.format(18-idade))
        print('Seu alistamento será em {}'.format(ano + 18))
elif idade > 18:
        rint('Você já deveria ter se alistado há {} anos'.format(idade-18))
        print('Seu alistamento foi em {}'.format(ano + 18))
elif idade == 18:
    print('Você deve se alistar imediatamente!')

