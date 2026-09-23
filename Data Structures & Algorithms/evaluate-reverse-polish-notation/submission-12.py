class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                first = stack.pop()
                stack.append(first + stack.pop())

            elif char == '-':
                first = stack.pop()
                stack.append(stack.pop() - first)

            elif char == '*':
                first = stack.pop()
                stack.append(first*stack.pop())

            elif char == '/':
                first = stack.pop()
                stack.append(int(stack.pop()/first))

            else:
                stack.append(int(char))


        return stack.pop()


        