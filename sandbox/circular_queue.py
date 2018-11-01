#!/usr/bin/env python3

class CircularQueue(list):
    def pop(self):
        if(len(self) > 0):
            ret = self[0]
            del self[0]
            return ret
    def push(self, x):
        self.append(x)

a = CircularQueue()

a.push(1)
print(a.pop())

