from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0

        def binarySearch(nums: List[int], target: int, offset: int) -> int:
            k = int((len(nums)-1)/2)
            if target == nums[k]:
                return k + offset
            elif len(nums) <= 1:
                return -1
            elif target < nums[k]:
                return binarySearch(nums[:k+1], target, offset)
            elif target > nums[k]:
                offset += k+1
                return binarySearch(nums[k+1:], target, offset)
            else:
                return -1
        return binarySearch(nums, target, offset)
