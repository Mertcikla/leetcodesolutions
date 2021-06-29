from typing import List


def plusOne(digits: List[int]) -> List[int]:
    s = ""
    a = []
    for c in digits:
        s += str(c)
    n = int(s)
    n += 1
    for c in str(n):
        a.append(c)
    return a
