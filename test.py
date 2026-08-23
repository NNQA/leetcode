from math import gcd
from functools import reduce

arr1 = [2, 3, 4, 5]
arr2 = [9, 12, 27, 30, 33]


row = 4
col = 0

for i in range(9):
    print("row", 3 * (row // 3) + i // 3)
for i in range(9):
    print("col", 3 * (col // 3) + i % 3)
