st = (input("Введите строку "))
st1 = (input("Введите искомую подстроку "))
le = len(st)

index = st.find(st1)
if index != -1:
    print("Индекс первого вхождение подстроки с начала строки -" + str(index))
else:
    print("Подстрока отсутствует в строке")

index1 = st.rfind(st1)

if index1 == index:
    print("Второе вхождение подстроки отсутствует")
else:
    print("Индекс последнего вхождение подстроки с начала строки -" + str(index1))

