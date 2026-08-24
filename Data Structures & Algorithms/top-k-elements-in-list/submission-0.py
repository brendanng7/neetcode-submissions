class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        maxHeap = [(a, b) for (b, a) in list(counter.items())]
        
        heapq.heapify_max(maxHeap)
        res = []
        for _ in range(k):
            p, element = heapq.heappop_max(maxHeap)
            res.append(element)
        return res