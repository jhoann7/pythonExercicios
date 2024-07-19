sal = float(input('Qual o valor do salário do funcionário: R$'))
if sal <= 1250:
    aumento = (sal / 100) * 15
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal + aumento))
else:
    aumento = (sal / 100) * 10
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal + aumento))