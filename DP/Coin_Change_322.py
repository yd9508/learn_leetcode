""""
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
class Solution:
    def coinChange(self, coins, amount):
        res = [0]

        for i in range(1, amount + 1):
            if i < min(coins):
                res.append(-1)
            elif i in coins:
                res.append(1)
            else:
                temp = []
                for coin in coins:
                    if coin < i:
                        if res[i - coin] == -1:
                            temp.append(-1)
                        else:
                            temp.append(res[i - coin] + 1)
                temp = [x for x in temp if x > 0]
                res.append(-1 if len(temp) == 0 else min(temp))

        return res[amount]