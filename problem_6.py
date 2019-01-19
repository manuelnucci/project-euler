def sum_of_the_squares(n):
    sum = 0
    for x in range(1, n+1):
        sum += x**2
    return sum


def square_of_the_sum(n):
    sum = n * (n+1) / 2
    return sum**2


number = 100
print(square_of_the_sum(number) - sum_of_the_squares(number))
