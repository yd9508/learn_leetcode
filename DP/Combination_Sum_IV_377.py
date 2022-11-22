"""
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""
# DP solution

class Solution:
    def combinationSum4(self, nums, target):
        res = [0] * (target + 1)
        for i in range(1, target + 1):
            for num in nums:
                if i - num == 0:
                    res[i] += 1
                elif i - num > 0:
                    res[i] += res[i - num]

        return res[-1]




# Recursion solution, exceed time limit, Using DP instead

# class Solution:
#     def combinationSum4(self, nums, target):
#
#         if target == 0:
#             return 1
#
#         if target < 0:
#             return 0
#
#         res = 0
#         for num in nums:
#             res += self.combinationSum4(nums, target - num)
#
#         return res