import math


def samp(q, n):
    r = 0.0

    for i in range(q):
        r += math.log((n-i)/n)
    
    return math.exp(r)

def coll(q, n):
    return 1 - samp(q, n)
