class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for string in strs:
            if string == "":
                encoded_arr.append("/")
            for c in string:
                encoded_arr.append(str(ord(c)))
                encoded_arr.append(",")
            encoded_arr.append(" ")
        return ''.join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        result = []
        decoded = s.split()
        for word in decoded:
            temp = word.split(",")
            temp.pop()
            string_arr = []
            for c in temp:
                string_arr.append(chr(int(c)))
            string = ''.join(string_arr)
            result.append(string)
        
        return result
