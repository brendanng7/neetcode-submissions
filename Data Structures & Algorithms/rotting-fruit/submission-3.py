class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        # find all the rotting oranges
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((0, x, y))

        if not queue:
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1:
                        return -1
            return 0

        while queue:
            time, x, y = queue.popleft()
            neighbours = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for neighbour in neighbours:
                r, c = neighbour
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    queue.append((time + 1, r, c))
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1
        
        return time

        
