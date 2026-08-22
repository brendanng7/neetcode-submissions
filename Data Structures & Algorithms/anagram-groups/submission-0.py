class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getAnagramKey(string):
            charArr = [0] * 26
            for c in string:
                charArr[ord(c) - 97] += 1
            return tuple(charArr)
        
        anagramDict = {}

        for string in strs:
            key = getAnagramKey(string)
            if key in anagramDict:
                anagramDict[key].append(string)
            else:
                anagramDict[key] = [string]
        
        return list(anagramDict.values())