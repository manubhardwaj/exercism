from math import pow

def on_square(integer_number):
    return pow(2,integer_number-1)

def total_after(integer_number):
    return sum([on_square(i) for i in xrange(1,integer_number+1)])
