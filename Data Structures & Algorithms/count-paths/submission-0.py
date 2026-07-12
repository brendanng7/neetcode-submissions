class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * m] * n

        for r in range(n):
            for c in range(m):
                if r == 0 or c == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[n-1][m-1]
