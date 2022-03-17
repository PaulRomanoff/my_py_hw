# HW 9
# Main class for creating stacks and popping values from it
class Queue:
    def __init__(self):
        # List that serves as stack
        self.Stack_list = []

    # Adding elements
    def put(self, val):
        self.Stack_list.append(val)

    # Deleting elements
    def get(self):
        try:
            val = self.Stack_list[-1]
            del self.Stack_list[-1]
            return val

    def __str__(self):
        return self.Stack_list

class QueueError(IndexError):
    def __init__(self, msg):
        IndexError.__init__(msg)
        pass

# def is_el_en(trig):
#     if trig:
#         raise QueueError
#     else:
#         raise IndexError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
print(que.__str__())
try:
    for i in range(4):
        print(que.get())
except IndexError:
    raise QueueError