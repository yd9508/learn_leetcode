"""
1566. Detect Pattern of Length M Repeated K or More Times
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
"""
from itertools import combinations
class Solution:
    def containsPattern(self, arr, m,k):
        all = list(combinations(arr, m))
        dic = {}
        for one in all:
            if one not in dic.keys():
                dic[one] = 1
            else:
                dic[one] = dic[one] + 1

        if k <= max(dic.values()):
            return True
        else:
            return False
