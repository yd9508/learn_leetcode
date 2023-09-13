### Using DP
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        # Create a 2D DP array to store the maximum score difference between players
        dp = [[0] * n for _ in range(n)]

        # Initialize the DP array with the values of nums
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill in the DP array diagonally
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        # If dp[0][n-1] is greater than or equal to 0, Player 1 can win
        return dp[0][n - 1] >= 0


#####
