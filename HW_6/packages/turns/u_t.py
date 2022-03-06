# user turns
def user_turn(board, checklist):
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