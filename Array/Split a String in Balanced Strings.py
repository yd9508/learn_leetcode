"""
1221. Split a String in Balanced Strings
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""


class Solution:
    def balancedStringSplit(self, s):
        if len(s) == 2:
            return 1 if s[1] != s[0] else 0

        for i in range(len(s)):


