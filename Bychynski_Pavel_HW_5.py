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

def user_turn(board = board, checklist = checklist):
        for row in board:
            for element in row:
                if type(element) == int not in row:
                    break
                else:
                    u_turn = int(input("enter the number of nonmaked box U want to mark: "))
                    if u_turn not in range (1, 10) or type(u_turn) != int or u_turn not in checklist:
                        print("incorrect box number")
                        continue
                    else:
                        for row_ch in board:
                            for element_ch in row_ch:
                                if element_ch == u_turn:
                                    board[row_ch][element_ch] = "O"
                            for c_elem in checklist:
                                if c_elem == u_turn:
                                    checklist[c_elem] = "O"

def comp_turn(board = board, checklist = checklist):
    import random
    for row in board:
        for element in row:
            if type(element) == int not in row:
                break
            else:
                c_turn = random.randint(1, 10)
                if c_turn not in row:
                    continue
                else:
                    for row in board:
                        for elem in row:
                            if elem == c_turn:
                                board[row][elem] = "X"
                        for c_elem in checklist:
                            if c_elem == c_turn:
                                checklist[c_elem] = "X"



display_board()
board[1][1] = "X"
checklist[4] = "X"
print(board)
print(checklist)
display_board()
user_turn()
print(board)
print(checklist)
display_board()
comp_turn()

    # for t_numb in range(1, 5):
    #     print(board)
    #     print(checklist)
    #     display_board()
    #     user_turn()
    #     print(board)
    #     print(checklist)
    #     display_board()
    #     comp_turn()