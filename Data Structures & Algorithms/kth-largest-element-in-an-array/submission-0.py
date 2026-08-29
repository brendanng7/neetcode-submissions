class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify_max(maxHeap)

        for num in nums:
            heapq.heappush_max(maxHeap, num)
        
        for i in range(k-1):
            heapq.heappop_max(maxHeap)
        
        return maxHeap[0]