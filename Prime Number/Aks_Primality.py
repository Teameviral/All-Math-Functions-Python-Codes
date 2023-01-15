import math

def power(x, y, p):

    res = 1

    x = x % p

    while y > 0:

        if y & 1:

            res = (res * x) % p

        y = y >> 1

        x = (x * x) % p

    return res

def is_prime(n):

    if n <= 1:

        return False

    if n <= 3:

        return True

    if n % 2 == 0 or n % 3 == 0:

        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):

        if n % i == 0 or n % (i + 2) == 0:

            return False

    r = int(math.sqrt(n))

    for a in range(2, r + 1):

        if power(a, n - 1, n) != 1:

            return False

    for r in range(2, r + 1):

        for a in range(1, r):

            x = (a * a) % (r * r)

            y = (a * a * a) % (n * r)

            if x == y:

                return False

    return True

