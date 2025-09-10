salario = float(input("Digite o seu salário: "))
tempo = int(input("Quanto tempo de empresa: "))

if salario < 2000 and tempo >= 5: 
    bonus = salario * 0.2
elif salario < 2000 and tempo < 5:
    bonus = salario * 0.1
elif salario >= 2000 and tempo >= 5:
    bonus = salario * 0.05
else:
    print("Sem bonus")

print("Seu bônus é de:",bonus)