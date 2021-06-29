from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myhash = defaultdict(int)
        for i in nums:
            myhash[i] += 1

        for i in myhash:
            if myhash[i] == 1:
                return i
