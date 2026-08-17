class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run bfs on each unvisited coordinate. mark visited on land we see on each iteration of bfs
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        totalIslands = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c]:
                    continue
                elif not visited[r][c] and grid[r][c] == "1":
                    totalIslands += 1
                    visited[r][c] = True
                    queue = deque([(r, c)])
                    while queue:
                        x, y = queue.popleft()
                        neighbours = [(x,y+1), (x+1,y), (x-1,y), (x,y-1)]
                        for n in neighbours:
                            if n[0] < 0 or n[0] >= len(grid):
                                continue
                            elif n[1] < 0 or n[1] >= len(grid[0]):
                                continue
                            elif visited[n[0]][n[1]]:
                                continue
                            elif grid[n[0]][n[1]] == "1":
                                visited[n[0]][n[1]] = True
                                queue.append(n)
                                
                    
                else:
                    visited[r][c] = True


        return totalIslands
        