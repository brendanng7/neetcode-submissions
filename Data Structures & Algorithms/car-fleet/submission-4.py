from heapq import heappush_max, heappop_max

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxHeap = []
        for i in range(len(position)):
            pos, sp = position[i], speed[i]
            heappush_max(maxHeap, (pos, sp))
        
        totalFleet = len(position)
        while maxHeap:
            firstCar = heappop_max(maxHeap)
            pos1, sp1 = firstCar
            timeToDest1 = (target - pos1) / sp1
            if maxHeap:
                carBehind = heappop_max(maxHeap)
                pos2, sp2 = carBehind
                timeToDest2 = (target - pos2) / sp2
                if timeToDest2 <= timeToDest1:
                    heappush_max(maxHeap, firstCar)
                    totalFleet -= 1
                else:
                    heappush_max(maxHeap, carBehind)
        
        
        return totalFleet