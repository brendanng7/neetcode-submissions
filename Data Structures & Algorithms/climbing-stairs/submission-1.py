class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        numWaysAtI = [0] * n
        numWaysAtI[0] = 1
        numWaysAtI[1] = 2
        for i in range(2, n):
            numWaysAtI[i] = numWaysAtI[i-1] + numWaysAtI[i-2]
        return numWaysAtI[n-1]