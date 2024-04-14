val1 = int((input("Введите число a ")))

val2 = int((input("Введите число в ")))


def gcd_recursive(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == 0:
        return max_num
    elif min_num == 1:
        return 1
    else:
        return gcd_recursive(min_num, max_num % min_num)

print(f"Наибольший общий делитель чисел {val1} и {val2} (рекурсия) {gcd_recursive(val1, val2)}")

def gcd_iter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b

print(f"Наибольший общий делитель чисел {val1} и {val2} (итерация) {gcd_iter(val1, val2)}")