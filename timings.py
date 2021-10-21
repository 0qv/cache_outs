import sys, timeit, cache_outs

sys.setrecursionlimit(2000)


@cache_outs.cache_outs
def fibonacci_cached(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

def fibonacci_uncached(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_uncached(n-1) + fibonacci_uncached(n-2)

def ackermann(m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m-1,1)
    return ackermann(m-1,ackermann(m,n-1))

@cache_outs.cache_outs
def ackermann_cache(m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann_cache(m-1,1)
    return ackermann_cache(m-1,ackermann_cache(m,n-1))



print("Cached: " + str(timeit.timeit(lambda: fibonacci_cached(42), number=1)))
print("Uncached: " + str(timeit.timeit(lambda: fibonacci_uncached(42), number=1)))




