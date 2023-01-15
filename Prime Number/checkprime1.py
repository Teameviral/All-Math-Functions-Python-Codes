def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n**(1/2))+1):

        if n % i == 0:

            return False

    return True

print(is_prime(2)) # True
print(is_prime(7)) # True
print(is_prime(15)) # False
