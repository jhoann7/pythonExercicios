val = float(input('Valor da casa: R$'))
sal = float(input('Valor do seu salário: R$'))
tempo = float(input('Em quantos anos você quer pagar: '))

pres = val / (tempo * 12)

print('O valor da parcela será de R${:.2f}'.format(pres)
      )
if pres > (sal / 100)*30:
    print('O valor da parcela excedeu o limite de 30% do seu salário!')
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO')
