poziom = int(input("Podaj liczbę całkowitą: "))
i = 1
while i <= poziom:
    ilosc_gwiazdek = 2 * i - 1
    gwiazdki = "*" * ilosc_gwiazdek
    ilosc_spacji = (poziom * 2) - 1
    print(gwiazdki.center(ilosc_spacji))
    i += 1