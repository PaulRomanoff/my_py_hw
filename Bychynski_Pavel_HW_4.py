# # CW_test
# def mass (num):
#     print("lul", num)
# num = 2
# mass(4)
# print(num)
#
# def dt (a=1, b=2):
#     mass(999)
#     print("line:", a, b)
# dt("check")
#
# def mult (f=1, s=1):
#     print("mult: ", f, "*", s, "=", f * s)
# t_n1 = int(input("1"))
# t_n2 = int(input("2"))
# mult(t_n1, t_n2)
#
# # 4.1
# # a bunch of defines for calculations
# def add ():
#     print(user_num_1, "+", user_num_2, "=", user_num_1 + user_num_2)
# def sub ():
#     print(user_num_1, "-", user_num_2, "=", user_num_1 - user_num_2)
# def mult ():
#     print(user_num_1, "*", user_num_2, "=", user_num_1 * user_num_2)
# def div ():
#     print(user_num_1, "/", user_num_2, "=", user_num_1 / user_num_2)
# def mod ():
#     print(user_num_1, "%", user_num_2, "=", user_num_1 % user_num_2)
# def exp ():
#     print(user_num_1, "**", user_num_2, "=", user_num_1 ** user_num_2)
# def fdiv ():
#     print(user_num_1, "//", user_num_2, "=", user_num_1 // user_num_2)
# # almost identical to previous calculatiors
# def maxi ():
#     minmax_l = []
#     i_numb = 1
#     minmax_numb = int(input("input amount of numbers (>1): "))
#     if minmax_numb > 1:
#         while i_numb <= minmax_numb:
#             num_e = int(input("input your number: "))
#             i_numb += 1
#             minmax_l.append(num_e)
#         print("max =", max(minmax_l))
#     else:
#         print("not enough elements")
# def mini ():
#     minmax_l = []
#     i_numb = 1
#     minmax_numb = int(input("input amount of numbers (>1): "))
#     if minmax_numb > 1:
#         while i_numb <= minmax_numb:
#             num_e = int(input("input your number: "))
#             i_numb += 1
#             minmax_l.append(num_e)
#         print("min =", min(minmax_l))
#     else:
#         print("not enough elements")
#
# print("That\'s a simple calculator")
# print(
#     """
#     Type \'add\' for addition, \'sub\' for subtraction,
#     \'mult\' for multiplication, \'div\' for division,
#     \'mod\' for modulus, \'exp\' for exponentiation, \'fdiv\' for floor division,
#     \'max\' to find the maximum number or \'min\' to find the minimum number.
#     Type \'exit\' to exit.
# """)
# oper = input()
# if oper == "add" or oper == "sub" or oper == "mult" or oper == "div" or oper == "mod" or oper == "exp" or oper == "fdiv":
#     user_num_1 = float(input("Type the first number: "))
#     user_num_2 = float(input("Type the second number: "))
#     if oper == "add":
#         add()
#     elif oper == "sub":
#         sub()
#     elif oper == "mult":
#         mult()
#     elif oper == "div":
#         div()
#     elif oper == "mod":
#         mod()
#     elif oper == "exp":
#         exp()
#     elif oper == "fdiv":
#         fdiv()
# elif oper == "max" or oper == "min":
#     if oper == "max":
#         maxi()
#     else:
#         mini()
# elif oper == "exit":
#     exit()
# else:
#     print("Invalid operation name")
#
# # 4.2
# def year_leap_or_not (y_year):
#     if y_year % 4 != 0:
#         return False
#     elif y_year % 100 != 0:
#         return True
#     elif y_year % 400 != 0:
#         return False
#     else:
#         return True
# # checking results
# test_data = [1900, 2000, 2016, 1987]
# test_result = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "->", end="")
#     result = year_leap_or_not(yr)
#     if result == test_result[i]:
#         print("OK")
#     else:
#         print("error")
# # for any year
# y_year = int(input("enter your year: "))
# if y_year >= 1582:
#     print(year_leap_or_not (y_year))
# else:
#     print("not within the Gregorian calendar period")

# 4.3
def days_in_month (month, yaer_result):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month ==10 or month == 12:
        print("31 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30 days")
    elif month == 2:
        if yaer_result == True:
            print("29 days")
        else:
            print("28 days")
    else:
        print("incorrect parameters")

def leap_or_not (y_year):
    if y_year % 4 != 0:
        return False
    elif y_year % 100 != 0:
        return True
    elif y_year % 400 != 0:
        return False
    else:
        return True

y_year = int(input("enter your year: "))
y_month = int(input("enter your month: "))
if y_month >= 1 and y_month <= 12:
    if y_year >= 1582:
        year_result = leap_or_not (y_year)
        print("is year leap?", year_result)
        days_in_month(y_month, year_result)
    else:
        print("not within the Gregorian calendar period")
else:
    print("incorrect number of month")

# 4.4
# lists for both types of year
leap_list = [31, 29, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
nonleap_list = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
sum_days = 0
# parameters from user
y_year = int(input("enter your year: "))
y_month = int(input("enter your month: "))
y_day = int(input("enter your day: "))
# Gregorian calendar check
if y_month >= 1 and y_month <= 12:
    if y_year >= 1582:
# True or Falce from leap_or_not def
        year_result = leap_or_not(y_year)
        print("is year leap?", year_result)
        if year_result == True:
# sum of days in months before user month
            for m_count in range(y_month - 1):
                sum_days += leap_list[m_count]
        else:
            for m_count in range(y_month - 1):
                sum_days += nonleap_list[m_count]
    else:
        print("not within the Gregorian calendar period")
else:
    print("incorrect number of month")
# number of days check
if y_month == 1 or y_month == 3 or y_month == 5 or y_month == 7 or y_month == 8 or y_month == 10 or y_month == 12:
    if y_day in range (1, 32):
        final_sum_days = sum_days + y_day
    else:
        print("incorrect numbers of days")
elif y_month == 4 or y_month == 6 or y_month == 9 or y_month == 11:
    if y_day in range (1, 31):
        final_sum_days = sum_days + y_day
    else:
        print("incorrect numbers of days")
elif month == 2:
        if yaer_result == True:
            if y_day in range (1, 30):
                final_sum_days = sum_days + y_day
            else:
                print("incorrect numbers of days")
        else:
            if y_day in range (1, 29):
                final_sum_days = sum_days + y_day
            else:
                print("incorrect numbers of days")
print("days sum =", final_sum_days)

#4.5