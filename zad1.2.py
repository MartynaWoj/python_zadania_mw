ktory_dzien_tygodnia = int(input("W który dzień tygodnia oddałeś buty do szewca? "))
ile_dni_naprawa = int(input("Ile dni będzie trwała naprawa? "))
po_ilu_dniach_zwrot = ile_dni_naprawa + ktory_dzien_tygodnia
dzien_tygodnia_zwrotu = po_ilu_dniach_zwrot % 7
print(f"Buty będą do odbioru {dzien_tygodnia_zwrotu} dnia tygodnia.")

