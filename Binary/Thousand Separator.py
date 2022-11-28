"""
1556. Thousand Separator
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
"""
class Solution1:
    def thousandSeparator(self, n):
        if n == 0:
            return "0"
        res = []
        count = 0
        while n != 0:
            a = n % 10
            n = n // 10
            if n != 0:
                count = count + 1
            else:
                res.append(str(a))
                break
            res.append(str(a))
            if count % 3 == 0:
                res.append(".")
        res.reverse()

        return "".join(res)
