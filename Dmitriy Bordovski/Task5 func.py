s = "May the Force be with you"

list = s.split()

print(list)

def len_word(a):
    """Эта функция считает длину самого короткого слова в строке. """

    m = len((min(a, key=len)))
    return m

print(f"Длина самого короткого слова - {len_word(list)}")
