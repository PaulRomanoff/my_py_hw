# 2.1
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# 2.2
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# 2.2*
print("    *", "     *", sep="       ")
print("   * *", "   * *", sep="       ")
print("  *   *", "  *   *", sep="      ")
print(" *     *", " *     *", sep="     ")
print("***   ***", "***   ***", sep="    ")
print("  *   *", "  *   *", sep="      ")
print("  *   *", "  *   *", sep="      ")
print("  *****", "  *****", sep="      ")

# 2.2**
print("    *\n   * *\n  *   *\n *     *")
print(3 * "*", 3 * "*", sep="   ")
print("  *   *\n  *   *\n  *****")

# 2.3
print(
    """
    \"I\'m\"
    \"\"learning\"\"
    \"\"Python\"\"
""")

# 2.4
# ввод числа фруктов у каждого человека
John_n = int(input("Фруктов у Джона: "))
Mary_n = int(input("Фруктов у Мэри: "))
Adam_n = int(input("Фруктов у Адама: "))
# нахождение суммарного кол-ва фруктов
fruits_sum = John_n + Mary_n + Adam_n
# вывод результатов
print("Фруктов у каждого соответственно: ")
print(John_n, Mary_n, Adam_n, sep=",")
print("Фруктов всего: \n", fruits_sum)

# 2.5
# базовые величины (можно обойтись и просто числами 1, 1.61)
mile = 1
km = mile * 1.61
# выбор требуемой конвертации величин
inp_dist = int(input("Для перевода mile -> km введите \'1\' \nДля перевода km -> mile введите \'2\' \n:"))
# первод в километры
if inp_dist == 1:
    inp_mile = float(input("Введите значение в mile: "))
    if inp_mile >= 0:
        result_temp = (inp_mile * km) / mile
        result = round(result_temp, 2)
        print(result, " km")
# проверка введенного числа миль
    else:
        print("Введено неверное значение (<0)")
# первод в мили
elif inp_dist == 2:
    inp_km = float(input("Введите значение в km: "))
    if inp_km >= 0:
        result_temp = (inp_km * mile) / km
        result = round(result_temp, 2)
        print(result, " mile")
# проверка введенного числа километров
    else:
        print("Введено неверное значение (<0)")
# проверка выбора конвертации
else:
    print("Введено неверное значение (введите 1 или 2)")

# 2.6
x = float(input("Введите х"))
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print(y)

# 2.7
second = 1
hourS = 3600
day = 24 * hourS
inp_hour = int(input("Input number of hours: "))
result_sec = inp_hour * hourS
print("There are",result_sec, "seconds in", inp_hour, "hour(s)")

# 2.8
print("That\'s a simple calculator for operations with two numbers")
num_1 = float(input("Type the first number: "))
num_2 = float(input("Type the second number: "))
print("Your first number", num_1,"Your second number", num_2)
print(
    """
    Type \'add\' for addition, \'sub\' for subtraction,
    \'mult\' for multiplication, \'div\' for division,
    \'mod\' for modulus, \'exp\' for exponentiation or \'fdiv\' for floor division.
""")
oper = input()
if oper == "add":
    result_C = num_1 + num_2
elif oper == "sub":
    result_C = num_1 - num_2
elif oper == "mult":
    result_C = num_1 * num_2
elif oper == "div":
    result_C = num_1 / num_2
elif oper == "mod":
    result_C = num_1 % num_2
elif oper == "exp":
    result_C = num_1 ** num_2
elif oper == "fdiv":
    result_C = num_1 // num_2
else:
    print("Invalid operation name")
result = round(result_C, 4)
print("Result: ",result)

# 2.9
x = 6
print("x = 6")
y = 1 / (6 + (1 / (6 + 1 / (6 + 1 / 6))))
print("y = ", y)

# 2.10 XD
print("Hello world")

# 2.11-15
y = 11111 * 1111111
print(y)
# can't divide by 0
y = 2014 ** 14
print(y)
month = 30 * 24 * 3600
print("There are",month, "seconds in 30 days")