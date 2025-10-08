import utils

idade  = int(input("Digite a sua idade: "))
renda = float(input("Digite a renda mensal: "))
dividas = float(input("Digite o valor total das dívidas: "))

if renda > 0:         # Verifica se a renda é maior que 0 para evitar divisão por zero
    perc_divida = (dividas / renda) * 100  # Calcula a porcentagem que as dívidas representam em relação à renda
else:
    perc_divida = 100 # Se a renda for zero, assume-se dívida em 100%, ou seja, situação de risco máximo

print(perc_divida)

if renda < 2000 and perc_divida > 50:
    risco = "Alto"
elif (2000 <= renda <= 5000) or (30 <= perc_divida <= 50):
    risco = "Médio"
elif renda > 5000 and perc_divida < 30:
    risco = "Baixo"
else:
    risco = "Médio-Baixo"

print(risco)
