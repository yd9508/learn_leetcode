"""
1572. Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""


class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        sum = 0
        for i in range(n):
            sum = sum + mat[i][i]
            sum = sum + mat[n - 1 - i][i]

        if n % 2 != 0:
            sum = sum - mat[n//2][n//2]

        return sum
