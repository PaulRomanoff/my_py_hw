# Lect 9 CW testing
# 9.1
class Huge:
    pass

class Big(Huge):
    pass

class Small(Big):
    pass

for cls1 in [Huge, Big, Small]:
    for cls2 in [Huge, Big, Small]:
        print(issubclass(cls1, cls2), end="\t")
    print()
print()

cake_huge = Huge()
cake_big = Big()
cake_small = Small()

for ob in [cake_huge, cake_big, cake_small]:
    for cls in [Huge, Big, Small]:
        print(isinstance(ob, cls), end="\t")
    print()
print("\n")

# 9.2
class SampleClass:
    def __init__(self, val):
        self.val = val

object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "We'll dream of Neo-Tokyo "
string_2 = "We'll dream of Neo-Tokyo tonight"
string_1 += "tonight"

print(string_1 == string_2, string_1 is string_2)
print("\n")

# 9.3
class Supa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Supa):
    def __init__(self, name):
        # Supa.__init__(self, name)
        super().__init__(name)

objct = Sub("Andy")
print(objct)
print("\n")

# 9.4
class Sup_cl:
    supVar = 1

class Sub_cl(Sup_cl):
    subVar = 2

obj = Sub_cl()

print(obj.subVar)
print(obj.supVar)
print("\n")

# 9.5
class Level1:
    varbl_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    varbl_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202

class Level3(Level2):
    varbl_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302

obj = Level3()

print(obj.varbl_1, obj.var_1, obj.fun_1())
print(obj.varbl_2, obj.var_2, obj.fun_2())
print(obj.varbl_3, obj.var_3, obj.fun_3())
print("\n")

class One:
    def dew_it(self):
        print("dew_it from One")

    def doanything(self):
        self.dew_it()

class Two(One):
    def dew_it(self):
        print("dew_it from Two")

one = One()
two = Two()

one.doanything()
two.doanything()
print("\n")

# 9.6
import time
class Tracks:
    def ch_direction(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def ch_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.ch_direction(left, True)
        time.sleep(0.25)
        self.controller.ch_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
print("\n")

# 9.7
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("GOODBYE THEN")
        return n

print(reciprocal(2))
print()
print(reciprocal(0))
print("\n")

# 9.8
try:
    i = int("Hi")
except Exception as e:
    print(e)
    print(e.__str__())
print("\n")

def print_ex_tree(thisclass, nest = 0):
    if nest > 1:
        print("    |" * (nest - 1), end="")
    if nest > 0:
        print("    +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_ex_tree(subclass, nest + 1)

print_ex_tree(BaseException)
print("\n")

# 9.9
class MyZDE(ZeroDivisionError):
    pass

def do_the_div(mine):
    if mine:
        raise  MyZDE("some worse news")
    else:
        raise ZeroDivisionError("some bad news")

for mode in [False, True]:
    try:
        do_the_div(mode)
    except ZeroDivisionError:
        print("Division by zero")

for mode in [False, True]:
    try:
        do_the_div(mode)
    except MyZDE:
        print("My DbZ")
    except ZeroDivisionError:
        print("original DbZ")