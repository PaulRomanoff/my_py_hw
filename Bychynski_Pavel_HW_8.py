# Lecture 8 HW
# Main class for creating stacks and popping values from it
class MStack:
    # Constructor
    def __init__(self):
        # List that serves as stack
        self.__PriStack_list = []
    # Adding elements
    def push_m(self, val):
        self.__PriStack_list.append(val)
    # Deleting elements
    def pop_m(self):
        val = self.__PriStack_list[-1]
        del self.__PriStack_list[-1]
        return val
# Subclass with new/updated counting functions
class CountingStack(MStack):
    def __init__(self):
        MStack.__init__(self)
        self.__sum = 0
        self.__in_count = 0
        self.__out_count = 0
    # Returns the sum of steck elements
    def get_sum(self):
        return self.__sum

    def push_m(self, val):
        # Counters for overall sum and added elements only sum
        self.__sum += val
        self.__in_count += val
        MStack.push_m(self, val)

    def pop_m(self):
        val = MStack.pop_m(self)
        # Counters for overall sum and popped elements only sum
        self.__sum -= val
        self.__out_count += val
        return val

    # Returns the sum of added elements
    def in_count(self):
        return self.__in_count

    # Returns the sum of popped elements
    def out_count(self):
        return self.__out_count

newStack_object = CountingStack()

for i in range(50):
    newStack_object.push_m(i)
    newStack_object.pop_m()
    # shows added and popped values after each iteration
    print("added", newStack_object.in_count())
    print("popped", newStack_object.out_count())
# line to show difference in added and popped values
newStack_object.push_m(57)
print("added", newStack_object.in_count())
print("popped", newStack_object.out_count())
print("sum", newStack_object.get_sum())
print()
