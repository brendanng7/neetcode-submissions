class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # bcabcdae
        hashset = set()
        longestlength = 0
        l = 0
        for r, letter in enumerate(s):
            while letter in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(letter)
            longestlength = max(longestlength, len(hashset))
        return longestlength
            
