wzrost = (float(input("Podaj swój wzrost w cm: ")))/100
masa = float(input("Podaj swoją masę ciała w kg: "))
bmi = masa/(wzrost**2)
if bmi<16:
    kategoria = "wygłodzenie"
elif bmi < 16.99:
    kategoria = "wychudzenie"
elif bmi < 18.49:
    kategoria = "niedowaga"
elif bmi < 24.99:
    kategoria = "waga prawidłowa"
elif bmi < 29.99:
    kategoria = "nadwaga"
elif bmi < 34.99:
    kategoria = "I stopień otyłości"
elif bmi < 39.99:
    kategoria = "II stopień otyłości"
elif bmi > 40:
    kategoria = "otyłość skrajna"
else:
    print("Dane są nieprawidłowe.")

print(f"Twoje BMI wynosi: {bmi:.2f}. Twoja kategoria: {kategoria} ")

#mniej niż 16 - wygłodzenie
#16 - 16.99 - wychudzenie
#17 - 18.49 - niedowaga
#18.5 - 24.99 - wartość prawidłowa
#25 - 29.99 - nadwaga
#30 - 34.99 - I stopień otyłości
#35 - 39.99 - II stopień otyłości
#powyżej 40 - otyłość skrajna