class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # iterate through each cell
        # find a treasure chest '0'
        # run breadth first traversal on each treasure chest
        # replace the element in grid only if curr dist away is lower
        m, n = len(grid), len(grid[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        def bfs(starts):
            queue = deque(starts)

            while queue:
                x, y, currDist = queue.popleft()  
                if visited[x][y] == True or grid[x][y] == -1:
                    continue
                if currDist < grid[x][y]:
                    grid[x][y] = currDist
                visited[x][y] = True
                neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for neighbour in neighbours:
                    r, c = neighbour
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    else:
                        queue.append((r, c, currDist + 1))
                    
        starts = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    starts.append((r, c, 0))
        bfs(starts)
        
