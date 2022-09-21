"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n):
        arr = [1, 2]
        if n == 1:
            return 1

        if n == 2:
            return 2

        for i in range(2, n):
            arr.append(arr[i - 2] + arr[i - 1])

        return arr[n - 1]