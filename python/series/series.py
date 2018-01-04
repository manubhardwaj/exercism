def slices(series, length):

    if(length > len(series) or length == 0):
        raise ValueError("String too short!")

    return [[int(i) for i in series[j:(j + length)]] for j in range(len(series) - length + 1)]
