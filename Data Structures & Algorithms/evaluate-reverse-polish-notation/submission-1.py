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
                if f < 0:
                    stack.append(math.ceil(f))
                else:
                    stack.append(math.floor(f))
            else:
                stack.append(int(token))
        return stack[-1]