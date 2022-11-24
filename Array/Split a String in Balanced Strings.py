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

        res = 0

        head = 0
        tail = 1

        while head < len(s):
            if self.isBalanceStr(s[head:(tail + 1)]):
                res  = res + 1
                head = tail + 1
                tail = tail + 2
            else:
                if tail < len(s):
                    tail = tail + 1
                else:
                    return res

        return res


    def isBalanceStr(self, s):
        dic = {}
        dic["L"] = 0
        dic["R"] = 0
        for i in range(len(s)):
            if s[i] == "L":
                dic["L"] = dic["L"] + 1
            else:
                dic["R"] = dic["R"] + 1

        if dic["R"] == dic["L"]:
            return True
        else:
            return False
