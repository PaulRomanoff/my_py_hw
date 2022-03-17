# pizza time
''' Unique error for pizza issues '''
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

class Pizza():
    def make_pizza(self, pizza, cheese):
        if pizza not in ["margherita", "capricciosa", "calzone"]:
            raise PizzaError (pizza, "pizza not in menu")
        if cheese > 100:
            raise TooMuchCheeseError (pizza, cheese, "to much cheese")
        print("Pizza ready!")

pizza_obj = Pizza()

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        pizza_obj.make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ":", tmce.cheese)
    except PizzaError as pe:
        print(pe, ":", pe.pizza)

