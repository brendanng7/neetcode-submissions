class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(r, c, i):
            letter = word[i]
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            if board[r][c] != letter:
                return False
            if (r, c) in visited:
                return False
            if i == len(word) - 1 and board[r][c] == letter:
                return True
            else:
                print(r, c, i)
                visited.add((r, c))
                neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                res = False
                for neighbor in neighbors:
                    res |= dfs(neighbor[0], neighbor[1], i + 1)
                visited.remove((r, c))
                return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
                visited.clear()

        
        return False
        
        