class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, num_open, num_close):
            if num_close < num_open or num_open < 0 or num_close < 0:
                return
            elif num_close == 0 and num_open == 0:
                res.append("".join(curr))
            else:
                curr.append("(")
                backtrack(curr, num_open - 1, num_close)
                curr.pop()
                curr.append(")")
                backtrack(curr, num_open, num_close - 1)
                curr.pop()
        
        backtrack([], n, n)
        return res
