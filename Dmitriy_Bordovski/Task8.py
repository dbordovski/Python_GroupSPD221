st = (input("Введите строку "))
pr = 0
symbol = 0

for char in st:
    if char == " ":
        pr += 1
    else:
        symbol += 1

print("В строке " + str(pr) + " пробелов и " + str(symbol) + " других символов")