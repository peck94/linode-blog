def prime(c):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    return primes[ord(c) - ord('a')]

def anagram_linear(s, t):
    if len(s) != len(t):
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    for c in alphabet:
        d[c] = 0
    for c1, c2 in zip(s, t):
        d[c1] += 1
        d[c2] -= 1
    for c in d:
        if d[c] != 0:
            return False
    return True
