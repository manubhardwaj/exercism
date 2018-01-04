def flip(i):
    if(ord(i) >= 65 and ord(i) <= 90):
        return chr(145-ord(i))
    elif(ord(i) >= 90 and ord(i) <= 122):
        return chr(212-ord(i))

    return i

def cipher(text):
    return str([flip(i) for i in text])

def encode(plain_text):
    return cipher(plain_text)

def decode(ciphered_text):
    return cipher(ciphered_text)
