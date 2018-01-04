from operator import mul

def largest_product(series, len):
    if len < 0:
        raise ValueError
    digits = [int(d) for d in series]
    groups = [tuple(digits[i:(i + len)]) for i in range(len(digits) - len + 1)]
    return max(reduce(mul, item, 1) for item in set(groups))
