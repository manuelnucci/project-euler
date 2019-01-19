from functools import reduce

xxxx_digit_number = ("73167176531330624919225119674426574742355349194934"
                     "96983520312774506326239578318016984801869478851843"
                     "85861560789112949495459501737958331952853208805511"
                     "12540698747158523863050715693290963295227443043557"
                     "66896648950445244523161731856403098711121722383113"
                     "62229893423380308135336276614282806444486645238749"
                     "30358907296290491560440772390713810515859307960866"
                     "70172427121883998797908792274921901699720888093776"
                     "65727333001053367881220235421809751254540594752243"
                     "52584907711670556013604839586446706324415722155397"
                     "53697817977846174064955149290862569321978468622482"
                     "83972241375657056057490261407972968652414535100474"
                     "82166370484403199890008895243450658541227588666881"
                     "16427171479924442928230863465674813919123162824586"
                     "17866458359124566529476545682848912883142607690042"
                     "24219022671055626321111109370544217506941658960408"
                     "07198403850962455444362981230987879927244284909188"
                     "84580156166097919133875499200524063689912560717606"
                     "05886116467109405077541002256983155200055935729725"
                     "71636269561882670428252483600823257530420752963450")


def largest_product_in_a_series(number, adjacent_digits):
    top = len(number) - adjacent_digits + 1
    max_product = 0

    list = []
    for c in number:
        list.append(int(c))

    i = 0
    while i in range(0, top):
        product = 1
        for j in range(i, i+adjacent_digits):
            if list[j] == 0: # We ignore the zeros and continue from the next value onwards
                i = j + 1
                break
            else:
                product *= list[j]
                if product > max_product:
                    max_product = product
                    factors = list[i:i+adjacent_digits]
        i += 1

    return max_product, factors

    # Another possibility using reduce and list comprehensions
    # This solution does not ignore zeros and compute all the products, leaving the search for the maximum for the last
    # return max([reduce(lambda x, y: x * y, list[i:i+adjacent_digits]) for i in range(len(list)-adjacent_digits)])


print(largest_product_in_a_series(xxxx_digit_number, 13))
