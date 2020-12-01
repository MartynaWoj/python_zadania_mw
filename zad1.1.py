ile_za_kg = float(input("Ile kosztuje kilo ziemniaków? "))
kg = 5
cena = ile_za_kg * kg
print(f"{kg} kg ziemniaków kosztuje {cena:.2f} zł.")

print('-'*30)

ile_za_kg = float(input("Ile kosztuje kilo ziemniaków? "))
kg = float(input("Ile kilo chcesz kupić? "))
cena = ile_za_kg * kg
print(f"{kg:.0f} kg ziemniaków kosztuje {cena:.2f} zł.")

print('-'*30)

ile_za_kg_ziemniakow = float(input("Ile kosztuje kilo ziemniaków? "))
kg_ziemniakow = float(input("Ile kilo ziemniaków chcesz kupić? "))
ile_za_kg_bananow = float(input("Ile kosztuje kilo bananów? "))
kg_bananow = float(input("Ile kilo bananów chcesz kupić? "))

cena_ziemniaki = ile_za_kg_ziemniakow * kg_ziemniakow
cena_banany = ile_za_kg_bananow * kg_bananow

do_zaplaty = cena_ziemniaki + cena_banany
print(f"Za {kg_ziemniakow:.1f} kg ziemniaków i {kg_bananow:.1f} kg bananów trzeba zapłacić {do_zaplaty:.2f} zł.")

if cena_ziemniaki > cena_banany:
    o_ile_wiecej_za_ziemniaki = cena_ziemniaki - cena_banany
    print(f"Więcej trzeba zapłacić za ziemniaki o {o_ile_wiecej_za_ziemniaki} zł.")
else:
    o_ile_wiecej_za_banany = cena_banany - cena_ziemniaki
    print(f"Więcej trzeba zapłacić za banany o {o_ile_wiecej_za_banany:.2f} zł.")