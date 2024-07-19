'''nome = str(input('Digite seu nome: '))
if nome.upper() == 'JHOANN':
    print('Você é muito lindo')
    print('Tenha um ótimo dia {}.'.format(nome))
else:
    print('Você não é lindo igual o jhoan')
    print('Tenha um bom dia {}, mas não melhor que o do Jhoann.'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

if m >= 5:
    print('Sua média foi de {:.1f}, parabéns, você foi aprovado!!!'.format(m))
else:
    print('Sua média foi de {:.1f}, infelizmente você reprovou!'.format(m))