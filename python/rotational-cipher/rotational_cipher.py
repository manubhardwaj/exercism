def rotate(text, key):
    rotated = ""
    for i in text:
        if str(i).isupper():
            number = (ord(i) - 65 + key) % 26
            rotated += chr(number + 65)
        elif str(i).islower():
            number = (ord(i) - 97 + key) % 26
            rotated += chr(number + 97)
        else:
            rotated += i

    return rotated

