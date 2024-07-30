print('-='*10)
print('CADASTRE UMA PESSOA')
print('-='*10)
cont = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
         cont += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F ]')).strip().upper()[0]
        if sexo == 'M':
             homem += 1
        elif sexo == 'F':
             if idade < 18:
                  mulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
            break
print(f'Você cadastrou {cont} pessoas com mais de 18 anos')
print(f'Você cadastrou {homem} homens')
print(f'{mulher} mulheres tem menos de 18 anos')

