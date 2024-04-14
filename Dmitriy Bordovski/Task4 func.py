val = (input("Введите число "))

def category(a):

    if int(a) > 0:
        rez = "положительное"
    else:
        if int(a) < 0:
            rez = "отрицательное "
        else:
            rez = "ноль"

    return rez


def digit(b):
    b = int(b) / 10
    raz = 0
    while b != 0:
            raz += 1
            b = int(b) / 10

    if int(val) == 0:
        raz = 1

    return raz

print(f"Число {val} {category(val)} количество разрядов - {digit(val)}")
