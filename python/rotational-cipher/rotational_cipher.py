def f(c,key):
    cint = ord(c)

    if(cint < 65):
        pass
    elif (cint > 122):
        pass
    elif (cint > 90 and cint < 97):
        pass
    else:
        if (cint >= 97):
            cint = cint + key
            if(cint > 122):
                cint -= 26
        else:
            cint = cint + key
            if(cint > 90):
                cint -= 26

    return chr(cint)



def rotate(text, key):
    return "".join(f(c,key) for c in text)
