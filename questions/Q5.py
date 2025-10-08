import utils

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(input("Type the day: "))
month = int(input("Type the month: "))
year = int(input("Type the year: "))

if (utils.leap_year(year)):
    dias_por_mes[1] = 29 

if 1 <= month <= 12 and 1 <= day <= dias_por_mes[month - 1] and year>0:
    print("The date is valid")
else:
    print("The date is not valid")