import utils

while True:
    try:
        idade = int(input("Digite sua Idade: "))
        if idade <= 0:
            raise "error"
        break
    except:
        print("Digite uma idade válida!")
        continue

if idade >= 16:
    while True:
        try:
            nacionalidade = int(input("Qual sua nacionalidade?\n1)Brasileiro\n2)Estrangeiro\n"))
            if nacionalidade != 1 and nacionalidade != 2:
                raise "error"
            break
        except:
            print("Digite uma opção válida!")
            continue

    if idade >= 18 and nacionalidade == 1:
        print("O voto é obrigatório!")
    else:
        print("O voto é opcional.")
else:
    print("Não pode votar!")