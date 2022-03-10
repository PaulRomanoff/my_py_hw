# tasks from lecture 7 CW
# 1
try:
    val = int(input("Enter a number: "))
    print("The reciprocal of", val, "is", 1 / val)
except ValueError:
    print("Don't know what to do")
except ZeroDivisionError:
    print("Can't divide bu 0")
except:
    print("something where wrong")

# 2
while True:
    try:
        numb = int(input("Enter an integer number: "))
        print(numb / 2)
        break
    except:
        print("Wrong number entered, try again")
print("\n")

# 3
char_1 = "a"
char_2 = " "
x = 97
print(ord(char_1))
print(ord(char_2))
print(chr(x))
print("\n")

# 4
the_string = "simple text"
for lat in range(len(the_string)-1, -1, -1):
    print(the_string[lat], end=" ")
print("\n")

# 5
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[1::2])
print("a" in alpha)
print("1" in alpha)
print("\n")

# 6
print(min("aAAbByYzZ"))
t = 'The Knights Who Say "Ni"'
print('[' + min(t) +']' )
space = min(t)
print("is a space: ", "\"", space, "\"", sep="")
print(ord(space))
print("\n")

# 7
print("321 time is running out".index("n") + 1)
print("321 time is ruNning out".index("n") + 1)
print("abcdefaafcccf".count("a"))
print("\n")

# 8
st = "abcabc"
print(st, type(st), list(st))
print()

di = {1: "one", 2: "two"}
print(di, type(di), list(di))
print()

tupl = ("1", "2")
print(tupl, type(tupl), list(tupl))
print("\n")

# 9
print("minsk".capitalize())
print('[' + '0w0'.center(13, '_') + ']')
t_end = "Hollywood"
print(t_end.endswith("wood"))
print(t_end.endswith("d"))
print(t_end.endswith("D"))
print(t_end.endswith("mood"))
print("\n")

# 10
print("Eta".find("ta"))
print("Eta".find("tatata"))
print("\n--------------------")
test_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et volutpat est. Pellentesque rutrum 
                tellus maximus efficitur porta. Morbi eleifend tincidunt cursus. Quisque ultrices neque lectus, vitae 
                efficitur velit placerat vitae. Curabitur congue eros id mauris mattis laoreet. Nullam ultricies enim 
                id risus scelerisque, in finibus massa fringilla. Maecenas elementum faucibus ullamcorper. Nunc 
                volutpat, nisl at sodales egestas, neque justo.
            """
fnd = test_text.find("te")
while fnd != -1:
    print(fnd)
    fnd = test_text.find("te", fnd + 1)
print("--------------------\n")

# 11
print(test_text.isalnum())
gl_list = ["one", "2", "III"]
gl_str = ", ".join(gl_list)
print(gl_str)
print(gl_str.replace("one", 'один'))
print(gl_str.split())
