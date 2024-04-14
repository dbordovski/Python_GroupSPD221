lst = [1, 15, 35, 4, 1, 15]


def make_unique(*args):
    tmp = sorted(list(set(*args)))
    return tmp

print(make_unique(lst))