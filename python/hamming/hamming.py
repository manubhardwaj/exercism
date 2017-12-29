def distance(strand_a, strand_b):
    if(len(strand_a) != len(strand_b)):
        raise ValueError("Strings not the same length!")

    distancae = 0
    for i in range(1,len(strand_a)):
        if(strand_a[:i+1] != strand_b[:i+1]):
            distancae += 1

    return distancae
