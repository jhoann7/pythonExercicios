s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    
    if s1 != s2 != s3 != s1:
        print('PODE FORMAR UM TRIÂNGULO ESCALENO!')
    elif s1 == s2 and s1 == s3:
        print('PODE FORMAR UM TRIÂNGULO EQUILÁTERO!')
    else:
        print('PODE FORMAR UM TRIÂNGULO ISÓRCELES!')
else:
    print('NÃO PODE FORMAR UM TRIÂNGULO!')