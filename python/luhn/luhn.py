from operator import mul
import re

class Luhn(object):
    def __init__(self, string):
        #strip it of non-numbers
        self.string = re.sub("[^0-9]","",string)

    def is_valid(self):
        digits = [int(d) for d in self.string[::-1]]
        for i in xrange(0,len(digits),2):
            digits[i] = 2*digits[i]
            if(digits[i]>9):
                digits[i] -= 9
        return (reduce(mul, digits, 1) % 10 == 0)
