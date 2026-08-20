class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter in "([{":
                stack.append(letter)
            elif letter in ")]}" and not stack:
                return False
            elif letter == ")" and stack.pop() != "(":
                return False
            elif letter == "]" and stack.pop() != "[":
                return False
            elif letter == "}" and stack.pop() != "{":
                return False
        return len(stack) == 0
                
                