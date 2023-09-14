class Solution:
    # Two pointers, sort the arr first, than two pointers, such the middle, it sum of head, tail and middle smaller than 0, middle += 1
    # else head -= 1;
    # Note, there are duplicate elements in the arr, handle that
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            if nums[i] + nums[low] + nums[high] < 0:
                low += 1
            elif nums[i] + nums[low] + nums[high] > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
