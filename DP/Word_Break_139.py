"""
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation
"""


class Solution:
    def wordBreak(self, s, wordDict):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]
