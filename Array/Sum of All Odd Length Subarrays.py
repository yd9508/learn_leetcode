"""
1588. Sum of All Odd Length Subarrays
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""


class Solution:
    def sumOddLengthSubarrays(self, arr):
        length = len(arr)
        res = 0
        for i in range(1, length + 1):
            if i  % 2 == 1:
                for j in range(length - i + 1):
                    res = res + sum(arr[j:(j + i)])

        return res
