from math import sqrt
num1 = float(input("Medida do cateto oposto: "))
num2 = float(input("Medida do cateto adjascnte: "))
print("A medida da hipotenusa é igual a {:.2f}".format(sqrt(num1**2 + num2**2)))