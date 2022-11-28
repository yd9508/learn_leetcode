"""
233. Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
"""
class Solution:
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones
