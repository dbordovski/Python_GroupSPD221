answer = []

print("Что визуально больше льва, но не весит и его когтя? ")
answer += input().split()
print("Зубы есть, а рта нет - что это? ")
answer += input().split()
print("Город, который может полететь? ")
answer += input().split()
print("Что снимают в Тик-Ток, чтобы набрать много просмотров? ")
answer += input().split()
print("Как подростки называют расслабленную, легкую атмосферу? ")
answer += input().split()

print(answer)

correct_answers = ("тень", "расческа", "Орел", "тренды", "чилл")

print(correct_answers)

total = {}

i = 0

while i < len(answer):
    if answer[i] == correct_answers[i]:
        total[correct_answers[i]] = 1
    else:
        total[correct_answers[i]] = 0
    i += 1

print(total)
