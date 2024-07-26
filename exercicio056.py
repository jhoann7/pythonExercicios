idad = 0
mediaidade = 0
maioridadehomem = 0
totmulher = 0
nomevelho = ''
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome da {}° pessoa: '.format(p)))
    idade = int(input('Idade da {}° pessoa: '.format(p)))
    sexo = str(input('Sexo {}° pessoa [M/F]: '.format(p))).strip()
    idad += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = idad / 4
print('A média de idade do grupo é de {:.1f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))