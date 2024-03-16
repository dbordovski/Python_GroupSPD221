number = int(input("Enter a three-digit number: "))
a = number // 100
b = (number - a * 100) // 10
c = number % 10
sum = a + b + c

print(sum)