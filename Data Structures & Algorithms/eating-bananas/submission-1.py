class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # logk n

        maxBanana = max(piles)
        minBanana = 1
        while minBanana < maxBanana:
            midBanana = minBanana + (maxBanana - minBanana) // 2
            
            hourEachPile = [math.ceil(numBanana / midBanana) for numBanana in piles]
            totalHours = sum(hourEachPile)
            if totalHours > h:
                minBanana = midBanana + 1
            else:
                maxBanana = midBanana

        return minBanana

        