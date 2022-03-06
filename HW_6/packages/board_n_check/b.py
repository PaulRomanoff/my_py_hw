# creates board and shows it
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(board)
print(checklist)
print("\n")

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")