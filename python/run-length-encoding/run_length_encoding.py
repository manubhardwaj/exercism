
import re

def decode(string):
    pattern = re.compile(r'([A-Z]+)([0-9]+)')
    retval = ''
    for (number, letter) in re.findall(pattern, string):
        retval += str(letter * int(number))

    return string(retval)

def encode(string):
    ls = [m.group(0) for m in re.finditer(r"(\d)\1*", string)]
    retval = ''
    for i in ls:
        retval += str(i[0]) + str(len(i))

    return str(retval)
