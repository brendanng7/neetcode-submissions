import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pointi in points:
            xi, yi = pointi
            dist = math.sqrt(xi**2 + yi**2)
            heapq.heappush(heap, (dist, pointi))
        
        return [point for dist, point in heapq.nsmallest(k, heap)]
