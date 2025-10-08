import utils

correct_sequence = ["B","C","D","A"]
entry = input("Type the sequence (Ex: ABCD): ").upper()
user_sequence = list(entry)

points = 0

for i in range(3):
    if user_sequence[i] == "C" and user_sequence[i+1] == "D":
        points += 5

for i in range(4):
    if user_sequence[i] == correct_sequence[i]:
        points += 10
    
    if user_sequence[i] == "A" :
        points += 5

print("Points: ",points)