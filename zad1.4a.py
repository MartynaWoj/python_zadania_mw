wiek = int(input("Podaj wiek: "))
ile_nocy = int(input("Ile noclegów spędzisz w hotelu: "))
if wiek < 18:
    cena = 100
elif wiek >= 18:
    if ile_nocy == 1:
        cena = 200
    elif 2 <= ile_nocy < 5:
        cena = 180
    else:
        cena = 150
if wiek >= 65:
    cena *= 0.9

print(f"Cena za jedną dobę w hotelu to {cena:.0f} zł, a za cały pobyt to: {cena * ile_nocy:.0f} zł.")
