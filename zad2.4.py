from random import randint

x = randint(0, 999)
i=0
while True:
    liczba = int(input("Zgadnij liczbę: "))
    if liczba > x:
        print("Liczba jest za duża!")
    elif liczba < x:
        print("Liczba jest za mała!")
    else:
        print("Gratulację, udało ci się odgadnąć liczbę za {ktora_proba} razem.")
        break
        i += 1
