val = (input ("Введите число "))

if int(val) > 0:
    rez = "положительное "
else:
    if int(val) < 0:
        rez = "отрицательное "
    else:
        rez = "ноль"

val1 = int(val) / 10
raz = 0
while val1 != 0:
    raz += 1
    val1 = int(val1) / 10

if int(val) == 0:
    raz = 1


print("Число " + str(rez) + " имеет " + str(raz) + " разр.")