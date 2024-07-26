from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('>>>>>Qual é a sua opção? '))

    if opcao == 1:
    
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} x {} é igual a {}'.format(n1, n2, mult))       
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))           
        elif n1 < n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))        
        else:
            print('Os dois números são iguais!')        
    elif opcao == 4:
        print('Informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao > 5 or opcao < 1:
        print('Opção inválida, tente novamente!')       
    print('=-=' * 10)
    sleep(1.5)
print('Finalizando...')
sleep(1.5)
print('Fim do programa')
print('=-=' * 10)
