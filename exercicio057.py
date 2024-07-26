s = ''
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
    print('Dados inválidos! Informe seu sexo: ')
if s == 'M':
    print('Sexo MASCULINO registrado com sucesso!')
else:
    print('Sexo FEMININO registrado com sucesso!')