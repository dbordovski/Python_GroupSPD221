class Soda:
    def __init__(self, topping):
        self.name = topping

    def show_my_drink(self):
        if self.name != "":
            return print(f"Газировка с {self.name} ")
        else:
            return print("Газировка с газом")


soda = Soda('Apple')
soda.show_my_drink()
soda = Soda('')
soda.show_my_drink()
