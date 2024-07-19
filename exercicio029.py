vel = float(input('Qual a velocidade que o carro estava: '))
if vel > 80:
    print('MULTADO, você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de {:.2f}R$'.format((vel-80)*7))
print('Tenha um bom dia, dirija com segurança!')