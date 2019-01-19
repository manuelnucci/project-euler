def special_pythagorean_triplet(n):
    values = [0, 0, 0]
    index = 0

    while not(pythagorean_triplet(values)) or sum(values) != n:
        values = update_list(values, index)
        index = update_index(index)
    return values


def pythagorean_triplet(values):
    return values[0]**2 + values[1]**2 == values[2]**2


def update_list(values, index):
    values[index] += 1
    return values


def update_index(index):
    return 0 if index == 2 else index + 1


print(special_pythagorean_triplet(1000))
