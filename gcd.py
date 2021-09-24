"""
>>> gcd(6, 9)
3
>>> gcd(98, 56)
14
>>> gcd_rec(6, 9)
3
>>> gcd_rec_two(98, 56)
14

gcd(a, b) == gcd(b, a) == gcd(b, remainder of a / b)

gcd(a, 0) == a
gcd(0, b) == b

gcd(a, b) = gcd(b - a, b) if b > a else gcd(a, a - b)
a % b = a if b > a else a - b
"""


def gcd(m, n):
    i = 1
    res = None

    while True:
        mq, mr = m // i, m % i
        nq, nr = n // i, n % i

        if mr == 0 and nr == 0:
            res = i

        if mq == 0 or nq == 0:
            break

        i = i + 1


    return res

def gcd_rec(m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if n == m:
        return n

    if m > n:
        return gcd_rec(m - n, n)

    return gcd_rec(m, n - m)


def gcd_rec_two(m, n):
    if n == 0:
        return m

    return gcd_rec_two(n, m % n)
