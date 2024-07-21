peso = float(input('Qual o peso: (Kg)'))
alt = float(input('Qual a altura: (m)'))

imc = peso / (alt**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Você está no peso normal, continue assim!')
elif 25 <= imc < 30:
    print('Você está acima do peso!')
elif 30 <= imc < 40:
    print('Você está em um nível de obesidade, tome cuidado!')
else:
    print('Você está em um caso de obesidade mórbida, procure se tratar!')