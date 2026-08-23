class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue = deque()
                    queue.append((r, c))
                    grid[r][c] = 0
                    currMax = 1
                    while queue:
                        x,y = queue.popleft()
                        neighbours = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
                        for n in neighbours:
                            if n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0]):
                                continue
                            elif grid[n[0]][n[1]] == 1:
                                queue.append(n)
                                grid[n[0]][n[1]] = 0
                                currMax += 1
                    res = max(res, currMax)
        return res