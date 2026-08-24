class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for element, freq in counter.items():
            bucket[freq].append(element)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for e in bucket[i]:
                    k -= 1
                    res.append(e)
                    if k == 0:
                        return res
        
        return res