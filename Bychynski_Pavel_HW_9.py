# HW 9
# Main class for creating stacks and popping values from it
class Queue:
    def __init__(self):
        # List that serves as stack
        self.__Stack_list = []

    # Adding elements
    def put(self, val):
        self.__Stack_list.append(val)

    # Deleting elements
    def get(self):
        val = self.__Stack_list[-1]
        del self.__Stack_list[-1]
        return val

    def __str__(self):
        return self.__Stack_list

class QueueError(IndexError):
    pass

    def is_el_en(self, trig):
        if trig:
            raise QueueError
        else:
            raise IndexError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
print(que.__str__())
try:
    for i in range(4):
        print(que.get())
except IndexError:
    QueueError.is_el_en(3 - 4)