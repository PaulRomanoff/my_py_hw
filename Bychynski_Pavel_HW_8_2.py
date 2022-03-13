# 8.2 "Timer"
class Timer:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s
        try:
            assert self.h in range(0, 24) and self.m in range(0, 60) and self.s in range(0, 60)
        except AssertionError:
            print("incorrect values - setting default values")
        except:
            print("something where wrong - setting default values")

    # def __str__(self):
    #     return self.h, self.m,  self.s

    def next_s(self):
        if self.s != 59:
            self.s += 1
        else:
            self.s = 0
            if self.m != 59:
                self.m += 1
            else:
                self.m = 0
                if self.h != 23:
                    self.h += 1
                else:
                    self.h = 0

    def prev_s(self):
        if self.s != 0:
            self.s -= 1
        else:
            self.s = 59
            if self.m != 0:
                self.m -= 1
            else:
                self.m = 59
                if self.h != 0:
                    self.h -= 1
                else:
                    self.h = 23

    def s_dual(self, val):
        s = str(val)
        if len(s) == 1:
            s = "0" + s
        return s

    def __str__(self):
        return Timer.s_dual(self.h, self.h) + ":" + Timer.s_dual(self.m, self.m) + ":" + Timer.s_dual(self.s, self.s)



test_t = Timer(22, 7, 59)
print(test_t.__str__())
test_t.next_s()
print(test_t.__str__())
test_t.prev_s()
print(test_t.__str__())