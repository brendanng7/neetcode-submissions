class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        charArr = [0] * 26
        for letter in s:
            charArr[ord(letter) - 97] += 1
        for letter in t:
            charArr[ord(letter) - 97] -= 1
        
        return all(count == 0 for count in charArr)