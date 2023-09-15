class Solution:
    def numIslands(self, grid):
        """
        Question: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
        return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.
        :param grid:
        :return componentCounter:

        Recursively use the DFS method, once a 1 is located, changed it to -1 and use DFS to find any 1 whcih is adjacent to it
        """
        componentCounter = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            grid[i][j] = -1
            if (i < m - 1 and grid[i + 1][j] == "1"):
                dfs(i + 1, j)
            if (i > 0 and grid[i - 1][j] == "1"):
                dfs(i - 1, j)
            if (j < n - 1 and grid[i][j + 1] == "1"):
                dfs(i, j + 1)
            if (j > 0 and grid[i][j - 1] == "1"):
                dfs(i, j - 1)

        for k in range(m):
            for l in range(n):
                if grid[k][l] == "1":
                    componentCounter += 1
                    dfs(k, l)
        return componentCounter
