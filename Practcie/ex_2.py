number = int(input())

if number % 2 == 0:
    print("Число является чётным")
else:
    print("Число является нечётным")

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

if 10 <= number <= 50:
    print("Число принадлежит диапазону [10, 50]")
else:
    print("Число не принадлежит диапазону [10, 50]")
