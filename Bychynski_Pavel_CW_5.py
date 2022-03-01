# CW examples test: 5.1
def test_funct():
    var = 222
    print("222 variable inside: ", var)

var = 1
test_funct()
print("new var outside", var, "\n")

# 5.2.1
def list_test_def(my_list_1):
    print("1) ", my_list_1)
    print("2) ", my_list_2)
    my_list_1 = [0, 1]
    print("3) ", my_list_1)
    print("4) ", my_list_2)

my_list_2 = [2, 3]
list_test_def(my_list_2)
print("5) ", my_list_2, "\n")
# 5.2.2 (new def)
def list_test_def_2(my_list_1):
    print("1) ", my_list_1)
    print("2) ", my_list_2)
    del my_list_1[0]
    print("3) ", my_list_1)
    print("4) ", my_list_2)

my_list_2 = [2, 3]
list_test_def_2(my_list_2)
print("5) ", my_list_2, "\n")

# 5.3
gft_name = "old"
print(gft_name)

def global_function_test():
    global gft_name
    gft_name = "new"
    return  gft_name

print(global_function_test())
# gft_name value changed in function
print(gft_name, "\n")

# 5.4
def bmi (weight, height):
    if weight <= 0 or height <= 0:
        return None
    else:
        return round((weight / height ** 2), 5)

print(bmi(0,0))
print(bmi(-99, 184))
print(bmi(80, 184))
print("\n")

# 5.5.1
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))
print("\n")

# 5.5.2
def fib_funct (n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_funct(n - 1) + fib_funct(n - 2)

for n in range(1, 10):
    print(n, "->", fib_funct(n))
print("\n")

# 5.6
test_tuple = (1, 3, True, "NO")
tt1 = test_tuple + ("No", "no")
tt2 = test_tuple * 4
print(len(test_tuple))
print(tt1)
print(tt2)
print("no" in test_tuple)
print("Yes" not in test_tuple)
print("\n")

# 5.7
test_dictionary = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
}
print(test_dictionary)
print(test_dictionary["cat"])
print("\n")

test_words = ["cat", "dog", "lion"]
for word in test_words:
    if word in test_dictionary:
        print(word, "->", test_dictionary[word])
    else:
        print(word, "is not in dictionary")
print("\n")

for eng, fr in test_dictionary.items():
    print(eng, "->", fr)
for eng, fr in test_dictionary.items():
    print(eng)
for fr in test_dictionary.values():
    print(fr)
print("\n")

test_dictionary.update({"duck": "canard"})
print(test_dictionary)
print("\n")

# 5.8
school_class = {}

while True:
    name = input("enter the student's name: ")
    if name == "":
        break

    score = int(input("enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score, )
    else:
        school_class[name] = (score, )

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += scoregit
        counter += 1
    print(name, ":", adding / counter)