# 3.1
hat_list = [1, 2, 3, 4, 5]
print(hat_list)
print("length of list is ", len(hat_list))
mid_replacer = int(input("enter your number to replace the middle one in this list: "))
# replacing element "3" with user number
hat_list[2] = mid_replacer
# deleting last element
del hat_list[-1]
print("length of new list is ", len(hat_list))
print(hat_list)

# CW ex
ex_list = [10, 1, 8, 3, 5]
ex_length = len(ex_list)
print(ex_length)
for i in range(ex_length // 2):
    ex_list[i], ex_list[ex_length - i - 1] = ex_list[ex_length - i - 1], ex_list[i]
print(ex_list)

# 3.2
beatles_list = []
beatles_list.append("John Lennon")
beatles_list.append("Paul McCartney")
beatles_list.append("George Harrison")
# user hint
print("need two more beatles: Stu Sutcliffe and Pete Best")
# "while" batter then "for" in this example so user needs to input correct artists names
while len(beatles_list) <5:
    artist_name = input("add another artist: ")
    if artist_name == "Stu Sutcliffe" or artist_name == "Pete Best":
        beatles_list.append(artist_name)
    else:
        print("that's not beatles artist")
        continue
print(beatles_list)
# deleting Stu Sutcliffe and Pete Best from the list
del beatles_list[-1]
del beatles_list[-1]
# adding Ringo Starr to the list
beatles_list.insert(0, "Ringo Starr")
print("beatles members later", beatles_list)

# 3.3
numb_in_l = int(input("how many numbers do you want in the list? "))
numb_list = []
# creating user list with append method
for i in range (numb_in_l):
    numb_el = float(input("input element (number): "))
    numb_list.append(numb_el)
print("your list", numb_list)
# reverse sort option
s_method = input("standard option is increased sort, enter \'r\' if U want reversed sort or just press \'ENTER\'")
# sort trigger
swapped = True
while swapped:
    swapped = False
    for j in range(numb_in_l - 1):
        if s_method == "r":
# reversed sort
            if numb_list[j] < numb_list [j + 1]:
                swapped = True
                numb_list[j], numb_list[j + 1] = numb_list[j + 1], numb_list[j]
        else:
# increased sort
            if numb_list[j] > numb_list [j + 1]:
                swapped = True
                numb_list[j], numb_list[j + 1] = numb_list[j + 1], numb_list[j]
print("sorted list: ", numb_list)

# 3.4
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)
new_list = []
# trigger
unic = True
for elem in range(len(my_list)):
    unic = False
# adds element from my_list to new_list if it's not already there
    if my_list[elem] not in new_list:
        new_list.append(my_list[elem])
        elem = True
print(new_list)

# 3.5
elems_n = input("enter your numbers (example: 2 12 78 4) \n: ")
spl_list = elems_n.split()
for i in range(len(spl_list)):
    spl_list[i] = int(spl_list[i])
print("your list: ", spl_list)
sum_l = 0
for element in range(len(spl_list)):
    sum_l += spl_list[element]
print("sum =", sum_l)

# 3.6
el_fin = input("enter your numbers (example: 2 12 78 4) \n: ")
sp_list = el_fin.split()
for i in range(len(sp_list)):
    sp_list[i] = int(sp_list[i])
print("your list: ", sp_list)
sp_list.sort()
print(sp_list)
fin_list_1 = []
fin_list = []
for a in range(len(sp_list) - 1):
    if sp_list[a] == sp_list[a + 1]:
        fin_list_1.append(sp_list[a])
un = True
for p in range(len(fin_list_1)):
    un = False
    if fin_list_1[p] not in fin_list:
        fin_list.append(fin_list_1[p])
        elem = True
print(fin_list)
# no time for 3.6+ :c