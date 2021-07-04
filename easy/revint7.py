class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(abs(x))[::-1])
        if abs(y) < math.pow(2, 31):
            if x < 0:
                return -1 * y
            else:
                return y
        else:
            return 0
