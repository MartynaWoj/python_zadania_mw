lista = [49, 50, 20, 40, 35, 10]

minimum = min(lista)
maksimum = max(lista)

lista[lista.index(minimum)] = maksimum
lista[lista.index(maksimum)] = minimum
minimum, maksimum = maksimum, minimum

print(f"{lista}")
