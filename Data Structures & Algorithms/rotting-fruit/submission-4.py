class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        time = 0
        while queue:
            levelLength = len(queue)
            for _ in range(levelLength):
                x, y = queue.popleft()
                neighbours = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
                for neighbour in neighbours:
                    r, c = neighbour
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                        continue
                    if grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))
            if queue:
                time += 1
        
        return time if fresh == 0 else -1

