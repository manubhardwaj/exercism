import collections
def is_pangram(sentence):
    d = collections.defaultdict(int)
    sentence = sentence.lower()
    for c in sentence:
        if(c.isalpha()):
            d[c] += 1

    if(len(d) == 26):
        return True

    return False
