"""
213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

# Compared with 198, using similiar method
# do it twice, for the first time, do it orderly, for the second time, do it reversely. For each time, neglect the last element, such that we can compare which results is larger.


class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        res1 = [nums[0]] * (len(nums) - 1)
        res1[1] = max(nums[0:2])

        for i in range(2, len(nums) - 1):
            res1[i] = max(res1[i - 2] + nums[i], res1[i - 1])

        temp1 = res1[-1]

        nums.reverse()

        res2 = [nums[0]] * (len(nums) - 1)
        res2[1] = max(nums[0:2])

        for i in range(2, len(nums) - 1):
            res2[i] = max(res2[i - 2] + nums[i], res2[i - 1])

        temp2 = res2[-1]

        return max(temp1, temp2)