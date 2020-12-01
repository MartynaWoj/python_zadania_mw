gracz_x = int(input("Podaj pozycję x: "))
gracz_y = int(input("Podaj pozycję y: "))

if not (0 <= gracz_x <= 100) or not (0 <= gracz_y <= 100):
    print("Jesteś poza planszą.")
if (90 <= gracz_x <= 100):
    if (0 <= gracz_y <= 10):
        print("Jesteś w prawym dolnym rogu.")
    elif (10 <= gracz_y <= 90):
        print("Jesteś na prawym boku.")
    else:
        print("Jesteś w prawym górnym rogu.")
if (0 <= gracz_x <= 10):
    if (0 <= gracz_y <= 10):
        print("Jesteś w lewym dolnym rogu.")
    elif (10 <= gracz_y <= 90):
        print("Jesteś na lewym boku.")
    else:
        print("Jesteś w lewym górnym rogu.")
if (10 <= gracz_x <= 90):
    if (0 <= gracz_y <= 10):
        print("Jesteś na dolnym boku.")
    elif (10 <= gracz_y <= 90):
        print("Jesteś na środku.")
    else:
        print("Jesteś na górnym boku.")
