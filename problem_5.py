def smallest_multiple(top):
    mcm = 1
    for number in range(2, top+1):
        mcm = minimum_common_multiple(mcm, number)
    return mcm


def minimum_common_multiple(x, y):
    a = max(x, y)
    b = min(x, y)

    while b:
        mcd = b
        b = a % b
        a = mcd
    return (x * y) // mcd


print(smallest_multiple(20))
