print('-='*10)
print('   LOJA JC LINDÃO')
print('-='*10)
total = 0
caro = 0
cont = 0
menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: R$'))
    total += preco
    cont += 1
    if preco > 1000.00:
         caro += 1
    if cont == 1:
         menor = preco
         barato = produto
    else:
         if preco < menor:
            menor = preco
            barato = produto
    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
            break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'Temos {caro} produto custando mais que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')