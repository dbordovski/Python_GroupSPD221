dic1 = ["a", "b", "c", "d"]
dic2 = [1, 2, 3, 4]

obj = {}

k = 0

for char in dic1:

    obj[char] = dic2[k]
    k += 1

print(obj)

