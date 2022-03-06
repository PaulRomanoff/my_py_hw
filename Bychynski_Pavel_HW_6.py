# "system info program"
# adding module
import platform
# functions for each user command
def py_ver_f():
    print(platform.python_version())

def os_f():
    print(platform.system())

def osv_f():
    print(platform.version())

def os_bitness_f():
    print(platform.machine())

def proc_f():
    print(platform.processor())

def exit_f():
    exit()

# program intro
print(
    """
    This program allows U to see your system info.
    1) To see your python version enter \'py\'
    2) To see your OS enter \'os\'; \'osv\' shows it's version
    3) To see bitness of your OS enter \'bit\'
    4) To see information about your processor enter \'proc\'
    5) To exit program print \'exit\'
    """
)
switch_ex = False
# input cycle, it can be interrupted with 'exit' command
while switch_ex == False:
    u_command = input("enter command: ")
    if u_command == "py":
        py_ver_f()
    elif u_command == "os":
        os_f()
    elif u_command == "osv":
        osv_f()
    elif u_command == "bit":
        os_bitness_f()
    elif u_command == "proc":
        proc_f()
    elif u_command == "exit":
        exit_f()
    else:
        print("incorrect command")
