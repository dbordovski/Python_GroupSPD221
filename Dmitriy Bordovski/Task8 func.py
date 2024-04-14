list1 = [1, 2, 3, 8, 9]

list2 = ['need', 'to', 'sleep', 'more']

list3 = [1]




def get_pairs(lst: list) -> list[tuple]:
        i = 0
        list11 = tuple()
        while i < len(lst)-1:
                list11 += (lst[i], lst[i+1])
                i += 1
        return list11

print(get_pairs(list1))

print(get_pairs(list2))

print(get_pairs(list3))