nota_zero = False
notas = []

while len(notas) < 3:
    nota_informada = 0
    while True:
        try:
            nota_informada = float(input("Informe a nota da prova:"))
            break
        except:
            print("Por favor insira um número válido (use pontos para decimais).")
            continue
    if nota_informada <= 0:
        nota_zero = True
        break
    notas.append(nota_informada)

if nota_zero:
    print("Reprovação automática por nota zero!")
else:
    media = sum(notas)/len(notas)
    if media >= 7:
        print("Aprovado!")
    elif media >= 5:
        print("Recuperação!")
    else:
        print("Reprovado!")
        
