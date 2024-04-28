class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.20462

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
            return self.__kg
        else:
            print('Килограммы должны быть числом')


a = KgToPounds(5)

b = a.to_pounds()
c = KgToPounds(20)
d = c.to_pounds()

print(b)
print(d)