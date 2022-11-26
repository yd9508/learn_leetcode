"""
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in dic.keys():
                dic[num] = [i]
            else:
                for j in range(len(dic[num])):
                    if abs(j - dic[num][j]) <= k:
                        return True
                dic[num].append(j)

        return False

