def even_Fibonacci_numbers(limit):
    sum = 0
    previous_number = 1
    next_number = 1
    while next_number < limit:
        if next_number % 2 == 0:
            sum += next_number
        aux = next_number
        next_number += previous_number
        previous_number = aux
        # print(f"{previous_number} {next_number}\n")
    return sum


print(even_Fibonacci_numbers(4000000))
