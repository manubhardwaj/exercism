def sum_of_multiples(limit, multiples):
    numbers = set()
    for multiple in multiples:
        for i in xrange(multiple,limit,multiple):
            numbers.add(i)
    return sum(numbers)

