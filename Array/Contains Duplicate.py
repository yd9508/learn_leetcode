"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums):
        dic  = {}
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                return True

        return False
