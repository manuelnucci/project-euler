def largest_palindrome_product(digits):
    min = int(10**(digits-1))
    max = int(10**digits) - 1
    # print(f'{min} {max}')
    ret = 0
    for i in range(max, min-1, -1):
        for j in range(i, min-1, -1):
            # print(f'{i} {j}')
            product = i * j
            if product < ret:
                break
            if is_palindrome(product):
                ret = product
                break
        if ret > (i-1)**2:
            break
    return ret


def is_palindrome(number):
    reversed_integer = reverse_integer(number)
    return number == reversed_integer


def reverse_integer(n):
    reversed_integer = 0
    while n != 0:
        remainder = n % 10
        reversed_integer = reversed_integer * 10 + remainder
        n //= 10
    return reversed_integer


print(largest_palindrome_product(3))
