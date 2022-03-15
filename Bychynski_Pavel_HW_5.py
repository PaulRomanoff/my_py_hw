# # 5.1
# # function for user numbers > 1
# def factorial_calc():
#     f_result = 1
#     for i in range (2, user_f_numb + 1):
#         f_result *= i
#     print(user_f_numb, "!", sep="", end=" ")
#     print("=", f_result)
#
# user_f_numb = int(input("enter your number to calculate it's factorial: "))
# # check for correct value type
# if type(user_f_numb) == int:
#     print("your number is", user_f_numb)
# else:
#     print("incorrect number value")
#     exit()
# if user_f_numb < 0:
#     print("incorrect number value")
#     exit()
# # 0 and 1 factorial without calculations
# elif user_f_numb < 2:
#     print(user_f_numb, "!", sep="", end=" ")
#     print("=", 1)
# else:
# # function for any numbers > 1
#     factorial_calc()
#     print("\n")
#
# # 5.2
# def fib_nums():
#     fib_1 = 1
#     fib_2 = 1
#     for f_numb in range (1, user_fib_n - 1):
#         fib_n = fib_1 + fib_2
#         print(fib_n)
#         fib_1, fib_2 = fib_2, fib_n
# user_fib_n = int(input("how many fib-numbers do you want?"))
# # check for correct value type
# if type(user_fib_n) == int:
#     print("your fib-numbers from fib_1 to fib", user_fib_n,":", sep="")
# else:
#     print("incorrect input")
#     exit()
# if user_fib_n < 0:
#     print("incorrect input")
#     exit()
# # 1 and 2 fib-numbers without calculations
# elif user_fib_n == 1:
#     print(1)
# elif user_fib_n == 2:
#     print(1)
#     print(1)
# # list of fib-numbers > 2
# else:
#     print(1)
#     print(1)
#     fib_nums()
# print("\n")

# 5.3
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(board)
print(checklist)
print("\n")

def display_board(board = board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

# function for users turns
def user_turn(board=board, checklist=checklist):
    turn_check = True
    while turn_check:
        u_turn = int(input("enter the number of nonmaked box U want to mark: "))
        if u_turn not in checklist:
            print("incorrect box number")
            continue
        else:
            turn_check = False
            checklist[u_turn - 1] = "O"
            if (u_turn - 1) // 3 == 0:
                big_l = 0
            elif (u_turn - 1 )// 3 == 1:
                big_l = 1
            elif (u_turn - 1) // 3 == 2:
                big_l = 2
            if u_turn % 3 == 1:
                mini_l = 0
            elif u_turn % 3 == 2:
                mini_l = 1
            elif u_turn % 3 == 0:
                mini_l = 2
            board[big_l][mini_l] = "O"

# program random turns
def comp_turn(board = board, checklist = checklist):
    import random
    c_turn_check = True
    while c_turn_check:
        c_turn = random.randint(1, 10)
        if c_turn not in checklist:
            continue
        else:
            c_turn_check = False
            checklist[c_turn - 1] = "X"
            if (c_turn - 1) // 3 == 0:
                big_l = 0
            elif (c_turn - 1 )// 3 == 1:
                big_l = 1
            elif (c_turn - 1) // 3 == 2:
                big_l = 2
            if c_turn % 3 == 1:
                mini_l = 0
            elif c_turn % 3 == 2:
                mini_l = 1
            elif c_turn % 3 == 0:
                mini_l = 2
            board[big_l][mini_l] = "X"

def win_check(checklist = checklist):
    win_b = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_b:
        if checklist[each[0]] == checklist[each[1]] == checklist[each[2]]:
            return print(checklist[each[0]], "win")
            break
    return False

display_board()
board[1][1] = "X"
checklist[4] = "X"
display_board()
user_turn()
for t_numb in range(1, 4):
    display_board()
    comp_turn()
    win_check()
    display_board()
    user_turn()
    win_check()
comp_turn()
display_board()
print(checklist)
print(board)
win_check()
