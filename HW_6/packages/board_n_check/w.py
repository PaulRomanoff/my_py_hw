# tt winner check
def win_check(checklist):
    win_b = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_b:
        if checklist[each[0]] == checklist[each[1]] == checklist[each[2]]:
            return print(checklist[each[0]], "win")
            break
    return False