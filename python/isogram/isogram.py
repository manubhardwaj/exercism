import collections


def is_isogram(string):
    d = collections.defaultdict(int)
    string = string.lower()
    for c in string:
        if(c.isalpha()):
            d[c] += 1
            if (d[c] > 1):
                return False
    return True
