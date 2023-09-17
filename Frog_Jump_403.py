class Solution:
    def canCross(self, stones):
        """
        My DP solution
        Time Limit Exceeded!!!
        :param stones:
        :return:
        """
        if stones[1] != 1:
            return False
        elif len(stones) == 2:
            return True
        plans = [[[1, 1]]]

        for i in range(2, len(stones)):
            plans.append([])
            for j in range(len(plans)):
                for k in range(len(plans[j])):
                    if stones[i] - plans[j][k][0] == plans[j][k][1]:
                        plans[i - 1].append([stones[i], plans[j][k][1]])
                    elif stones[i] - plans[j][k][0] == plans[j][k][1] + 1:
                        plans[i - 1].append([stones[i], plans[j][k][1] + 1])
                    elif stones[i] - plans[j][k][0] == plans[j][k][1] - 1:
                        plans[i - 1].append([stones[i], plans[j][k][1] - 1])

        return True if plans[len(stones) - 2] != [] else False

