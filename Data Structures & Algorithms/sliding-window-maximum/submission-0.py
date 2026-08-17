class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        for i in range(k):
            num = nums[i]
            maxHeap.append((num, i))
        heapq.heapify_max(maxHeap)
        maxElements = [maxHeap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush_max(maxHeap, (nums[i], i))
            removedIndex = i - k
            while True:
                maxElement = maxHeap[0]
                if maxElement[1] <= removedIndex:
                    heapq.heappop_max(maxHeap)
                else:
                    break
            maxElements.append(maxElement[0])
        return maxElements
        