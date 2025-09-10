preco = float(input("Preço do produto: "))
vip = input("É cliente VIP? (s/n): ")

if preco >= 100:
    desconto = 0.20
elif preco >= 50:
    desconto = 0.10
else:
    desconto = 0.0

if vip.lower() == "s":
    desconto += 0.05

print("Preço final:", preco * (1 - desconto))
