class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0

        def bfs(x, y):
            neighbours = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            grid[x][y] = "0"
            for neighbour in neighbours:
                if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]) and grid[neighbour[0]][neighbour[1]] == "1":
                    bfs(neighbour[0], neighbour[1])
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    numOfIslands += 1
                    bfs(r, c)

        return numOfIslands