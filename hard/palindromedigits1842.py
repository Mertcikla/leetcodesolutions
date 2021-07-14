from typing import List


def swap(num: List, i: int, j: int) -> List:
    s = num[i]
    num[i] = num[j]
    num[j] = s
    s = num[len(num)-i-1]
    num[len(num)-i-1] = num[len(num)-j-1]
    num[len(num)-j-1] = s
    return num


s = "leebeel"
p = []
p[:0] = s
print(swap(p, 0, 3))
