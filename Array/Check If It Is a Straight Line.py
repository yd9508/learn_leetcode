"""
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

class Solution:
    def checkStraightLine(self, coordinates):

        if len(coordinates) == 2:
            return True

        if coordinates[0][0] == coordinates[1][0]:
            intercept = coordinates[0][0]
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != intercept:
                    return False
            return True

        coeff = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        intercept = coordinates[0][1] - coeff * coordinates[0][0]

        for i in range(2, len(coordinates)):
            if coordinates[i][1] != intercept + coeff * coordinates[i][0]:
                return False

        return True




