peso = float(input("Qual o seu peso?\n"))

altura = float(input("Qual a sua altura? \n"))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Voce esta abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Voce possui o peso normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Voce esta em sobrepeso")
elif IMC >= 30 and IMC <= 34.9:
    print("Voce possui obesidade grau I")
elif IMC >= 35 and IMC <= 39.9:
    print("Voce possui obesidade grau II")
else:
    print("Voce possui obesidade grau III")