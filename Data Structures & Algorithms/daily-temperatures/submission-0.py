class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = [] # stack that is always increasing values
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while monostack and temp > temperatures[monostack[-1]]:
                past = monostack.pop()
                res[past] = i - past
            monostack.append(i)
        
        return res