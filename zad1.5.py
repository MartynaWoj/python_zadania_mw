import math
a = float(input("Długość pierwszego boku trójkąta: "))
b = float(input("Długość drugiego boku trójkąta: "))
c = float(input("Długość trzeciego boku trójkąta: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    pole_kwadrat = p * (p - a) * (p - b) * (p - c)
    pole = math.sqrt(pole_kwadrat)
    print(f"Pole trójkąta wynosi: {pole:.2f}.")
else:
    print("Nie można ułożyć trójkąta z podanych długości boków.")