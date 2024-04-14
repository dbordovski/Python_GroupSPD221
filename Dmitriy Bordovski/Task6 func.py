year = int((input("Введите количество лет для подсчета популяции лягушек в пруду ")))

def get_number_of_frogs(year: int) -> int:
    F_k = 120
    i = 1
    while i < year:
        F_k = 2*(F_k - 50)
        i += 1
    return F_k


print(f"Количество лягушек в пруду за {year} года(лет) - {get_number_of_frogs(year)}")