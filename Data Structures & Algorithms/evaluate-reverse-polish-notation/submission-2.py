class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                e1 = stack.pop()
                e2 = stack.pop()
                f = e2/e1
                stack.append(int(f))
            else:
                stack.append(int(token))
        return stack[-1]