"""
231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 2 or n == 1:
            return True
        if n % 2 == 1:
            return False
        else:
            return self.isPowerOfTwo(n // 2)
