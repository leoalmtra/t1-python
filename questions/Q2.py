import utils

lado1 = float(input("Me de o 1 lado\n"))

lado2 = float(input("Me de o 2 lado\n"))

lado3 = float(input("Me de o 3 lado\n"))

if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("O seu triangulo é Équilatero")
    else:
        print("O seu triangulo é isosceles")
else:
    print("O seu triangulo é escaleno")