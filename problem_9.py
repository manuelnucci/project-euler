import time

def special_pythagorean_triplet(n):
    for a in range(1, n):
     for b in range(a, n):
         c = n - a - b
         if c > 0:
             if c*c == a*a + b*b:
                 print(f'{a} {b} {c}')
                 return a*b*c

print(special_pythagorean_triplet(1000))
