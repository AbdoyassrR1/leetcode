#!/usr/bin/python3


def removeElement(nums, val):
    while val in  nums:
        nums.remove(val)
    k = len(nums)
    return k

nums = [0,1,2,2,3,0,4,2]
k = removeElement(nums, 2)
print(nums, k)
