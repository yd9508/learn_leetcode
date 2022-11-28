"""
1544. Make The String Great
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
"""
class Solution:
    def makeGood(self, s):
        if len(s) == 1:
            return s
        head = 0
        tail = 1
        temp = []
        while tail <= len(s) - 1:
            if abs(ord(s[tail]) - ord(s[head])) == 32:
                temp.append(head)
                temp.append(tail)
                if head != 0:
                    head = head - 1
                    tail = tail + 1
                else:
                    head = tail + 1
                    tail = tail + 2
            else:
                head = tail
                tail = tail + 1

        res = []
        for i in range(len(s)):
            if i not in temp:
                res.append(s[i])

        return "".join(res)
