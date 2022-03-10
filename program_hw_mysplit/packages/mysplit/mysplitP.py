# 7.1 manual split function
def mysplit_func():
# user can enter any text
    user_str = input("Enter your text: ")
# adding " " so last word 100% will be in the list
    user_str += " "
    s_list = []
    element = ""
    for el in user_str:
        if not el.isspace():
            element += el
        else:
# if there is number of " "
            if element != "":
                s_list.append(element)
                element = ""
            else:
                pass
    print(s_list)