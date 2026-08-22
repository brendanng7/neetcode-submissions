class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for string in strs:
            charArr = [0] * 26
            for c in string:
                charArr[ord(c) - ord('a')] += 1
            key = tuple(charArr)
            if key in anagramDict:
                anagramDict[key].append(string)
            else:
                anagramDict[key] = [string]
        
        return list(anagramDict.values())