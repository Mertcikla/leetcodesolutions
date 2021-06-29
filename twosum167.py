from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    a = 0
    b = 1
    while a < len(numbers):
        while b < len(numbers):
            if numbers[a]+numbers[b] == target:
                return [a+1, b+1]
            elif numbers[a]+numbers[b] > target:
                break
            else:
                b += 1
        a += 1
        b = a+1
