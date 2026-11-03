class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [set([i]) for i in range(n)]
        for edge in edges:
            ai, bi = edge
            aiNodeSet = biNodeSet = None
            for nodeSet in arr:
                if ai in nodeSet:
                    aiNodeSet = nodeSet
                if bi in nodeSet:
                    biNodeSet = nodeSet
                if aiNodeSet and biNodeSet:
                    break
            if aiNodeSet is not biNodeSet:
                arr.remove(biNodeSet)
                arr.remove(aiNodeSet)
                aiNodeSet = aiNodeSet.union(biNodeSet)
                arr.append(aiNodeSet)

        return len(arr)