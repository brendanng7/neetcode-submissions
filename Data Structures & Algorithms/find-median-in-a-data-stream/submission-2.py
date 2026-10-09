class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.maxHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) >= len(self.minHeap) + 2:
            shiftNum = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, shiftNum)
        if len(self.minHeap) >= len(self.maxHeap) + 2:
            shiftNum = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, shiftNum)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        else:
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        
        