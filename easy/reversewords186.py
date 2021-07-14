from typing import List


def reverseWords(s: List[str]) -> None:
    """
        Do not return anything, modify s in-place instead.
        """
    m = str(s).split()
    print(m)
    s.reverse()


s = ["t", "h", "e", " ", "s", "k", "y",
     " ", "i", "s", " ", "b", "l", "u", "e"]
reverseWords(s)
print(s)


print(1)
