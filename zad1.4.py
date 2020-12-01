wiek = int(input("Podaj wiek: "))
ile_nocy = int(input("Ile noclegów spędzisz w hotelu: "))
if wiek < 18:
    cena = 100
elif 18 <= wiek < 65 and ile_nocy == 1:
    cena= 200
elif 18 <= wiek < 65 and 2 <= ile_nocy < 5:
    cena = 180
elif 18 <= wiek < 65 and ile_nocy >= 5:
    cena = 150
elif wiek >= 65 and ile_nocy == 1:
    cena = 0.9 * 200
elif wiek >= 65 and 2 <= ile_nocy < 5:
    cena = 0.9 * 180
elif wiek >= 65 and ile_nocy > 5:
    cena = 0.9 * 150

print(f"Cena za jedną dobę w hotelu to {cena:.0f} zł, a za cały pobyt to: {cena * ile_nocy:.0f} zł.")