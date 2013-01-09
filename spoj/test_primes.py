
def primes_sieve2(limit):
    a = [True]*limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        print i, isprime
            yield i
            for n in xrange(

primes_sieve2(10)

"""
def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        print "factors:", factors
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

print primes_sieve(100)
"""
