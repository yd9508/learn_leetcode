class Solution:
    def climbStairs(self, n):
        """
        DP solution
        :param n:
        :return:
        """
        ans = [1, 2]
        if n <= 2:
            return ans[n - 1]

        for i in range(2, n):
            ans.append(ans[i - 1] + ans[i - 2])

        return ans[n - 1]

    # def climbStairs(self, n: int) -> int:
    #"""
    # recursion solution
    #"""
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
