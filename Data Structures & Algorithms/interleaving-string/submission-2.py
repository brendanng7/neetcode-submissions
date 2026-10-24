import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # i is a pointer for s1
        # j is a pointer for s2
        # k is a pointer for s3

        @functools.cache
        def canInterleave(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            if i < len(s1) and s3[k] == s1[i]:
                if canInterleave(i+1, j, k+1):
                    return True

            if j < len(s2) and s3[k] == s2[j]:
                if canInterleave(i, j+1, k+1):
                    return True
            
            return False

        
        return canInterleave(0, 0, 0)

