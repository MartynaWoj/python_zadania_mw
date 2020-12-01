from random import randint

x = randint(0, 99)
y = randint(0, 99)
print(f"Liczba x to: {x}, a liczba y to: {y}.")
suma = x + y



while True:
    suma_uzytkownik = int(input("Ile wynosi ich suma? "))
    if suma != suma_uzytkownik:
        print ("Suma niepoprawna. Spróbuj jeszcze raz.")
        continue
    if suma == suma_uzytkownik:
        print("Suma poprawna.")
    break

