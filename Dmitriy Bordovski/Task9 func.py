list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


from typing import List


def foo(lst: List[int]) -> List[int]:
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if j != i:
                product *= lst[j]
        result.append(product)
    return result


print(foo(list1))