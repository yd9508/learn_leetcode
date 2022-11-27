"""
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""


class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        pre = nums[0]
        res = [[pre]]
        for i in range(1, len(nums)):
            if nums[i] - pre == 1:
                res[len(res) - 1].append(nums[i])
            else:
                res.append([nums[i]])
            pre = nums[i]

        res2 = []
        for lst in res:
            if len(lst) == 1:
                res2.append(str(lst[0]))
            else:
                res2.append(str(lst[0]) + "->" + str(lst[len(lst) - 1]))

        return res2

