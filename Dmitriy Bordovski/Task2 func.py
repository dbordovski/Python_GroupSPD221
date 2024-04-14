def g(a):
    res = a + 2
    return res

t = int(input("Введите число: "))

def increase_g(b):
    return g(b) + 1

print(f"{t} + 2 != {increase_g(t)}")