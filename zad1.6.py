wiek = int(input("Wiek: "))
liczba_biletow = int(input("Podaj liczbę biletów: "))
if wiek < 6:
    cena = 0
elif wiek < 17:
    cena = 2.28
elif wiek < 64:
    cena = 3.80
else:
    cena = 1.90
print(f"Należność to: {liczba_biletow * cena:.2f}")
