# Lecture 8 CW examples
# 8.1
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Ohh no... ZDE")
except ArithmeticError:
    print("Oooops... AE")
print("END")

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooops... AE")
except ZeroDivisionError:
    print("Ohh no... ZDE")
print("END2")
print()

# 8.2
def bad_funct(n):
    try:
        return  1 / n
    except ArithmeticError:
        print("Arithmetic problem")
    return None

bad_funct(0)
print("Stop!")

def bad_funct2(n):
    return 1 / n

try:
    bad_funct2(0)
except ArithmeticError:
    print("Some arithmetic error happened")
print("EnD!")
print()

# 8.3
def Rbad_funct(n):
    try:
        return n / 0
    except:
        print("Meeeh inner")
        # rise only can be inside except
        raise

try:
    Rbad_funct(0)
except ArithmeticError:
    print("Outer error here")
print("THEEND")
print()

# 8.4
import math
x = float(input("enter a number: "))
try:
    assert x >= 0.0
    x = math.sqrt(x)
except AssertionError:
    print("incorrect number!!!")
print(x)

angle = int(input("enter an angle in degrees: "))
try:
    assert angle % 180 != 90
    print(math.tan(math.radians(angle)))
except AssertionError:
    print("Bad angle!")
print()

# 8.5
# from time import sleep
# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Interrupted with keyboard")

# 8.6 stacks
t_stack = []
def push_el(val):
    t_stack.append(val)

def t_pop():
    val = t_stack[-1]
    del t_stack[-1]
    return val

push_el(1)
push_el(2)
push_el(3)
print(t_stack)
print(t_pop())
print(t_pop())
print(t_pop())
print()

# 8.7 creating class
class MStack:
    def __init__(self):
        print("Hello there!")
        self.stack_list = ["one", 2, "III"]
        self.__PriStack_list = []

    def push_m(self, val):
        self.__PriStack_list.append(val)

    def pop_m(self):
        val = self.__PriStack_list[-1]
        del self.__PriStack_list[-1]
        return val

stack_object = MStack()
print(len(stack_object.stack_list))
# print(len(stack_object.__PriStack_list))
print()
stack_object.push_m(3)
stack_object.push_m(2)
stack_object.push_m(1)

print(stack_object.pop_m())
print(stack_object.pop_m())
print(stack_object.pop_m())
print()

class AddingStack(MStack):
    def __init__(self):
        MStack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push_m(self, val):
        self.__sum += val
        MStack.push_m(self, val)

    def pop_m(self):
        val = MStack.pop_m(self)
        self.__sum -= val
        return val

newStack_object = AddingStack()

for i in range(5):
    newStack_object.push_m(i)
print(newStack_object.get_sum())
print()

for i in range(5):
    print(newStack_object.pop_m())
print("\n")

# 8.8
class ExampleClass:
    ecounter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.ecounter += 1


print(ExampleClass.__dict__)
ex_obj_1 = ExampleClass()
ex_obj_2 = ExampleClass(2)
ex_obj_3 = ExampleClass(4)
print()

print("1.0", ex_obj_1.__dict__)
print("1.1", ex_obj_1.__dict__, ex_obj_1.ecounter)
print("2.0", ex_obj_2.__dict__)
print("2.1", ex_obj_2.__dict__, ex_obj_2.ecounter)
print("3.0", ex_obj_3.__dict__)
print("4.1", ex_obj_3.__dict__, ex_obj_3.ecounter)
print()
print(ExampleClass.__dict__)
print()
print(ex_obj_1.__dict__)
print("\n")

# 8.9
class HAClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 2

exha_obj = HAClass(1)
print(exha_obj.a)
if hasattr(exha_obj, 'b'):
    print(exha_obj.b)
print()
print(HAClass.__name__)
t_obj = HAClass(2)
print(type(t_obj))
print(type(t_obj).__name__)
print()

# 8.10
class MyCl:
    pass

obj = MyCl()
obj.a = 1
obj.b = 2
obj.i = 3
obj.real = 3.5
obj.int = 4
obj.z = 5

def incIntsI (obj):
    for name in obj.__dict__.keys():
        if name.startswith("i"):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)