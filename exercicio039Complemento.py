print('''Qual é o  seu sexo?
[M] Masculino
[F] Feminino''')
s = str(input('Sua opção: '))
if s.upper() == 'M':
    ano = int(input('Seu ano de nascimento: '))
    alis = ano + 18
    id = 2024 - ano

    print('Quem nasce em {} terá {} anos em 2024'.format(ano, id))

    if id > 18:
        print('Você já deveria ter se alistado!')

        print('Seu ano de alistamento foi em {}'.format(alis))
        print('Já fazem {} anos desde o seu alistamento'.format(2024 - alis))
    elif id == 18:
        print('Você deve se alistar imediatamente!')
    else:
        print('Você ainda não está na idade de se alistar!')
        print('Ainda faltam {} anos para o seu alistamento.'.format(18 - id))
        print('Seu ano de alistamento será em {}'.format(alis))
elif s.upper() == 'F':
    print('Você é mulher e não é obrigada a se alistar!')
else:
    print('Opcão inválida!')