nome = str(input('Digite um uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(nome.count('A')))
print('A letra "A" aparece a primeira vez na posição: {}'.format(nome.find('A') + 1))
print('A letra "A" aparece a ultima vez na posição: {}'.format(nome.rfind('A') + 1))