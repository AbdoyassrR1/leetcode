#!/usr/bin/python3
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        nums = list(set(nums))
        nums.sort()
        k = len(nums)
        for i in range(length - len(nums)):
            nums.append("_")
        return f"{k}, nums = {nums}"


print(Solution().removeDuplicates([1,1,2]))

print(Solution().removeDuplicates([1,1,1,1]))
print(Solution().removeDuplicates([0,0,1,1,2,2,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
 