"""
1217. Minimum Cost to Move Chips to The Same Position
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
"""
class Solution:
    def minCostToMoveChips(self, position):
        sum1 = 0
        sum2 = 0

        for i in range(len(position)):
            if position[i] % 2 == 1:
                sum1 = sum1 + 1
            else:
                sum2 = sum2 + 1

        return min(sum1, sum2)
