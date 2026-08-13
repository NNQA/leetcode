from math import gcd
from functools import reduce

arr1 = [2, 3, 4, 5]
arr2 = [9, 12, 27, 30, 33]

g = reduce(gcd, arr2)

print(g)
ans = None

for x in arr1:
    if g % x == 0:
        if ans is None or x < ans:
            ans = x

print(ans)
