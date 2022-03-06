# random program turns
def comp_turn(board, checklist):
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