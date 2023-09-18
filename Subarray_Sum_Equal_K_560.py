class Solution:
    def subarraySum(self, nums, k):
        """
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.
        :param nums:
        :param k:
        :return:
        """
        dic = {0: 1}
        sum = 0
        count = 0
        for num in nums:
            sum += num
            if (sum - k) in dic.keys():
                count += dic[sum - k]
            dic[sum] = 1 if sum not in dic.keys() else dic[sum] + 1

        return count

