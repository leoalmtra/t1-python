import utils

price = float(input("Preço do produto: "))
vip = input("É cliente VIP? (s/n): ")

if price >= 100:
    desconto = 0.20
elif price >= 50:
    desconto = 0.10
else:
    desconto = 0.0

if vip.lower() == "s":
    desconto += 0.05

print("Preço final:", price * (1 - desconto))
