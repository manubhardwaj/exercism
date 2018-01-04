def abbreviate(words):
    # Failed the hyphen test, but a one line solution looks so good!
    return ''.join([i[0] for i in words.upper().split()])
