from bisect import bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use two rounds of binary search
        # first round of binary search on the first column
        # second round of binary search on the row

        m = len(matrix[0])
        n = len(matrix)

        firstCol = [arr[0] for arr in matrix]
        i = bisect_right(firstCol, target) - 1
        j = bisect_right(matrix[i], target) - 1
        print(i, j)
        return matrix[i][j] == target
