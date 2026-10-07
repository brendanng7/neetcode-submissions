class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        canFlowPacific = [[False for _ in heights[0]] for _ in heights]
        for i in range(len(canFlowPacific[0])):
            canFlowPacific[0][i] = True
            queue.append((0, i))
        for j in range(len(canFlowPacific)):
            canFlowPacific[j][0] = True
            queue.append((j, 0))

        while queue:
            x, y = queue.popleft()
            neighbours = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for neighbour in neighbours:
                r, c = neighbour
                if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                    continue
                if heights[x][y] <= heights[r][c] and not canFlowPacific[r][c]:
                    canFlowPacific[r][c] = True
                    queue.append((r, c))

        canFlowAtlantic = [[False for _ in heights[0]] for _ in heights]
        for i in range(len(canFlowAtlantic[-1])):
            canFlowAtlantic[-1][i] = True
            queue.append((len(canFlowAtlantic) - 1, i))
        for j in range(len(canFlowAtlantic)):
            canFlowAtlantic[j][-1] = True
            queue.append((j, len(canFlowAtlantic[j]) - 1))
        
        while queue:
            x, y = queue.popleft()
            neighbours = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for neighbour in neighbours:
                r, c = neighbour
                if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                    continue
                if heights[x][y] <= heights[r][c] and not canFlowAtlantic[r][c]:
                    canFlowAtlantic[r][c] = True
                    queue.append((r, c))
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if canFlowPacific[r][c] and canFlowAtlantic[r][c]:
                    res.append([r, c])
        return res