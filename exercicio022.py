nome = str(input('Digite seu nome completo: ')).strip()

mai = nome.upper()
min = nome.lower()
tot = len(nome)
nom = nome.split()
pnom = nom[0]
let = len(nom[0])

print('Seu nome em maiúsculas é: {}'.format(mai))
print('Seu nome em minúsculas é: {}'.format(min))
print('Seu nome tem ao todo {} letras'.format(tot - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(pnom, let))