wzrost = (float(input("Podaj swój wzrost w cm: ")))/100
masa = float(input("Podaj swoją masę ciała w kg: "))
BMI = masa/(wzrost**2)
if BMI<16:
    kategoria = "wygłodzenie"
elif BMI < 16.99:
    kategoria = "wychudzenie"
elif BMI < 18.49:
    kategoria = "niedowaga"
elif BMI < 24.99:
    kategoria = "waga prawidłowa"
elif BMI < 29.99:
    kategoria = "nadwaga"
elif BMI < 34.99:
    kategoria = "I stopień otyłości"
elif BMI < 39.99:
    kategoria = "II stopień otyłości"
elif BMI > 40:
    kategoria = "otyłość skrajna"
else:
    print("Dane są nieprawidłowe.")

print(f"Twoje BMI wynosi: {BMI:.2f}. Twoja kategoria: {kategoria} ")

#mniej niż 16 - wygłodzenie
#16 - 16.99 - wychudzenie
#17 - 18.49 - niedowaga
#18.5 - 24.99 - wartość prawidłowa
#25 - 29.99 - nadwaga
#30 - 34.99 - I stopień otyłości
#35 - 39.99 - II stopień otyłości
#powyżej 40 - otyłość skrajna