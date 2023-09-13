class Solution:
    def spiralOrder(self, matrix):
        directions = {'right': (lambda i, j: [i, j + 1]),
                      'down': (lambda i, j: [i + 1, j]),
                      'left': (lambda i, j: [i, j - 1]),
                      'up': (lambda i, j: [i - 1, j])}
        m = len(matrix)
        n = len(matrix[0])

        temp = []

        direction = 'right'
        i = 0
        j = 0
        while i < m and i >= 0 and j >= 0 and j < n:
            temp.append([i, j])
            if len(temp) == n * m:
                break
            next = directions[direction](i, j)
            if next[0] == m or next[0] < 0 or next[1] == n or next[1] < 0 or next in temp:
                if direction == 'right':
                    direction = 'down'
                elif direction == 'down':
                    direction = 'left'
                elif direction == 'left':
                    direction = 'up'
                elif direction == 'up':
                    direction = 'right'
                [i, j] = directions[direction](i, j)
            else:
                [i, j] = directions[direction](i, j)

        ans = []
        for i in range(len(temp)):
            ans.append(matrix[temp[i][0]][temp[i][1]])
        return ans
if __name__ == '__main__':
    Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
