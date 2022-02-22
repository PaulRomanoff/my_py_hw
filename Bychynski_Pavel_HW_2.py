# # 3.1 goal is to find the largest of four numbers
# # control value (cv)
# largest_numb = -999999999999999.9
# # comparing first number with cv
# numb_1 = float(input("enter your first number: "))
# if numb_1 > largest_numb:
# # possible cv change
#     largest_numb = numb_1
# # comparing second number with cv
# numb_2 = float(input("enter your second number: "))
# if numb_2 > largest_numb:
# # possible cv change
#     largest_numb = numb_2
# # comparing third number with cv
# numb_3 = float(input("enter your third  number: "))
# if numb_3 > largest_numb:
# # possible cv change
#     largest_numb = numb_3
# # comparing fourth number with cv
# numb_4 = float(input("enter your fourth number: "))
# if numb_4 > largest_numb:
# # possible cv change
#     largest_numb = numb_4
# # result
# print("you entered: ", numb_1, numb_2, numb_3, numb_4)
# print("largest number is: ", largest_numb)
#
# # 3.2
# numb_1 = int(input("enter your first number: "))
# numb_2 = int(input("enter your second number: "))
# numb_3 = int(input("enter your third  number: "))
# numb_4 = int(input("enter your fourth number: "))
# # finding max value without "max" function
# if numb_1 >= numb_2:
#     if numb_1 >= numb_3:
#         if numb_1 >= numb_4:
#             print("max number is: ", numb_1)
#         else:
#             print("max number is: ", numb_4)
#     elif numb_3 >= numb_4:
#         print("max number in: ", numb_3)
#     else:
#         print("max number is: ", numb_4)
# elif numb_2 >= numb_3:
#     if numb_2 >= numb_4:
#         print("max number is: ", numb_2)
#     else:
#         print("max number is: ", numb_4)
# else:
#     if numb_3 >= numb_4:
#         print("max number is: ", numb_3)
#     else:
#         print("max number is: ", numb_4)
# # finding min value with "min" function
# num_min = min(numb_1, numb_2, numb_3, numb_4)
# print("min number is: ", num_min)
#
# # 3.3
# real_plant = "Spathiphyllum"
# y_plant = input("name the best plant ever: ")
# # correct answer
# if y_plant == "Spathiphyllum":
#     print("Yeah - Spathiphyllum is the beast plant ever!")
# # without apper "S"
# elif y_plant == "spathiphyllum":
#     print("No! I want a big Spathiphyllum!")
# # any other answer
# else:
#     print("Spathiphyllum! Not ", y_plant)
#
# # 3.4 a tax calculator
# # tax coefficient
# tax_ind = 0.15
# income_val = float(input("input the income: "))
# # incorrect input
# if income_val <= 0:
#     print("incorrect income value inputed")
# # real income and tax
# else:
#     real_income = income_val - income_val * tax_ind
#     tax_val = income_val * tax_ind
#     print("real income is: ", round(real_income, 1))
#     print("tax is: ", round(tax_val, 1))
#
# # 3.5 leap year recogniser
# y_year = int(input("enter a year: "))
# if y_year <= 1582:
#     print("not within the Gregorian calendar period")
# else:
#     if y_year % 4 != 0:
#         print(y_year, "is a common year")
#     elif y_year % 100 != 0:
#         print(y_year, "is a leap year")
#     elif y_year % 400 != 0:
#         print(y_year, "is a common year")
#     else:
#         print(y_year, "is a leap year")
#
# # 3.6
# # magicians number
# mag_numb = 57
# # muggles number
# y_numb = 1
# # loop until correct input
# while y_numb != mag_numb:
#     print("Ha ha! You're stuck in my loop!")
#     y_numb = int(input("guess the number to escape the loop: "))
# print("Well done, muggle! You are free now")
#
# # 3.7
# # time library import
# import time
# # counting to five
# for i in range (1,6):
# # 1 sec delay
#     time.sleep(1)
#     print(i, "Mississippi")
# time.sleep(1)
# print("Ready or not, here I come!")
#
# # 3.8 chupacabra loop
# # correct word to escape the loop
# correct_chupa = "chupacabra"
# # placeholder for input word
# y_word = "meeeh"
# while y_word != correct_chupa:
#     y_word = input("guess the word to exit the loop: " )
#     if y_word == "chupacabra":
#         break
# print("You've successfully left the loop")
#
# # 3.9
# user_word = str(input("input a word: "))
# # changing to upper register
# user_word = user_word.upper()
# # printing user word without vowels
# if len(user_word) > 1:
#     for l in user_word:
#         if l == "A":
#             continue
#         if l == "E":
#             continue
#         if l == "I":
#             continue
#         if l == "O":
#             continue
#         if l == "U":
#             continue
#         print(l)
# # if users word is too short
# else:
#     print("enter more then 1 letter")
#
# # 3.10 (3.9*)
# user_word = str(input("input a word: "))
# # changing to upper register
# user_word = user_word.upper()
# # var for final result
# without_vowels_res = ""
# # printing user word without vowels
# if len(user_word) > 1:
#     for l in user_word:
#         if l == "A":
#             continue
#         if l == "E":
#             continue
#         if l == "I":
#             continue
#         if l == "O":
#             continue
#         if l == "U":
#             continue
#         without_vowels_res = without_vowels_res + l
#     print(without_vowels_res)
# # if users word is too short
# else:
#     print("enter more then 1 letter")
#
# # 3.11 Lothar Collatz formula
# step = 0
# user_number = int(input("input any non-negative and non-zero number: "))
# if user_number <= 0:
#     print("incorrect number")
# else:
#     while user_number != 1:
#         if user_number % 2 == 0:
#             user_number = user_number / 2
#             print(int(user_number))
#             step += 1
#         else:
#             user_number = 3 * user_number + 1
#             print(int(user_number))
#             step +=1
#     else:
#         print("steps: ", step)
#
# # 3.12
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
#     num_1 = float(input("Type the first number: "))
#     num_2 = float(input("Type the second number: "))
#     if oper == "add":
#         result_C = num_1 + num_2
#     elif oper == "sub":
#         result_C = num_1 - num_2
#     elif oper == "mult":
#         result_C = num_1 * num_2
#     elif oper == "div":
#         result_C = num_1 / num_2
#     elif oper == "mod":
#         result_C = num_1 % num_2
#     elif oper == "exp":
#         result_C = num_1 ** num_2
#     elif oper == "fdiv":
#         result_C = num_1 // num_2
# elif oper == "max" or oper == "min":
#     minmax_l = []
#     i_numb = 1
#     minmax_numb = int(input("input amount of numbers: "))
#     while i_numb <= minmax_numb:
#         num_e = int(input("input your number: "))
#         i_numb +=1
#         minmax_l.append(num_e)
#     if oper == "max":
#         result_C = (max(minmax_l))
#     elif oper == "min":
#         result_C = (min(minmax_l))
# elif oper == "exit":
#     exit()
# else:
#     print("Invalid operation name")
# result = round(result_C, 4)
# print("Result: ",result)

# 3.13
bits = int('0101010101', 2)
setB = int('10010', 2)
res_b = bin(bits | setB)
print(res_b)

# 3.14
bits = int('0101010111', 2)
setB = int('10001', 2)
res_b = bin(bits & setB)
print(res_b)