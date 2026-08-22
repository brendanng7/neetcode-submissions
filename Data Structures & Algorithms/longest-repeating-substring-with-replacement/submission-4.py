class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slide the window, keeping track of frequency of letters. 
        # slide left when still majority letter and total sum of non-dominant letter is > than k
        # get this sum by r - l - num of majority letter

        maxLength = 0
        l = 0
        counter = {}
        maxf = 0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            maxf = max(maxf, counter[s[r]])

            while r-l+1-maxf > k:
                l += 1
                counter[s[l-1]] -= 1
            maxLength = max(maxLength, r-l+1)
            
        return maxLength

