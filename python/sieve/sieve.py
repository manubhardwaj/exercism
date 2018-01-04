def sieve(limit):
    primes = []
    non_primes = set()

    for i in range(2, limit+1):
        if i not in non_primes:
            primes.append(i)
            for a in range(i*i, limit+1, i):
                non_primes.add(a)
    return primes
