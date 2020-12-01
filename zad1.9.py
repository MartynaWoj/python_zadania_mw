liczby = 1
while liczby <= 100:
    if liczby % 3 == 0 and liczby % 5 != 0:
        print(f"{liczby} - Fizz")
    elif liczby % 5 == 0 and liczby % 3 != 0:
        print(f"{liczby} - Buzz")
    elif liczby % 3 == 0 and liczby % 5 == 0:
        print(f"{liczby} - FizzBuzz")
    else:
        print(f"{liczby}")
    liczby +=1