print('========JC IMPORTS======')

valor = float(input('Valor da sua compra: R$'))

print('FORMAS DE PAGAMENTO')
print('''[1] à vista no dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual a opção desejada: '))

if opcao == 1:
    print('Sua compra é de R${:.2f} e vai custar R${:.2f} no final'.format(valor, valor - (valor / 100) * 10))
elif opcao == 2:
    print('Sua compra é de R${:.2f} e vai custar R${:.2f} no final'.format(valor, valor - (valor / 100) * 5))
elif opcao == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} sem júros.'.format(valor, valor / 2))
elif opcao == 4:
    x = int(input('Em quantas vezes (até 18): '))
    if x <= 18:
        juros = (valor / 100) * 20
        print('Sua compra será parcelada em {:.2f}x de R${:.2f} COM JÚROS'.format(x, (valor + juros) / x))
        print('Sua compra de R${:.2f} custará R${:.2f} no final!'.format(valor, valor + juros))
    else:
        print('Opção inválida')
else:
    print('Opção inválida')