import math


def largest_prime_factor(n):
    x = n
    limit = math.floor(math.sqrt(n))
    i = 1
    while x != 1 and i < limit:
        i += 1
        # if x % i == 0 and is_prime(i):
        if x % i == 0 and is_prime(i):
            while x % i == 0:
                x /= i
    return i if x == 1 else n


def is_prime(n):
    limit = math.floor(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


print(largest_prime_factor(600851475143))
