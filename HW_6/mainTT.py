# tic-tac toe with packages
from packages.board_n_check import b
from packages.turns import u_t
from packages.turns import c_t
from packages.board_n_check import w

b.display_board(b.board)
b.board[1][1] = "X"
b.checklist[4] = "X"
b.display_board(b.board)
u_t.user_turn(b.board, b.checklist)
for u_t.t_numb in range(1, 4):
    b.display_board(b.board)
    c_t.comp_turn(b.board, b.checklist)
    w.win_check(b.checklist)
    b.display_board(b.board)
    u_t.user_turn(b.board, b.checklist)
    w.win_check(b.checklist)
c_t.comp_turn(b.board, b.checklist)
b.display_board(b.board)
print(b.checklist)
print(b.board)
w.win_check(b.checklist)