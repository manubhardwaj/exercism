import random, re, string

class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:

            self.key = ''.join(key for _ in range(100))

    def encode(self, text):
        coded = ''
        for i, val in enumerate(text):
            coded += chr((ord(val) + ord(self.key[i]) - 193)%26 + 96)
        return coded

    def decode(self, text):
        decoded = ''
        for i, val in enumerate(text):
            decoded += chr((ord(val) - ord(self.key[i]) + 1)%26 + 96)
        return decoded


class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, ''.join('d' for _ in range(100)))
