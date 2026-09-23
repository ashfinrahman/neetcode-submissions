class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                first = stack.pop()
                stack.append(first + stack.pop())
                print(stack)
            elif char == '-':
                first = stack.pop()
                stack.append(stack.pop() - first)
                print(stack)
            elif char == '*':
                first = stack.pop()
                stack.append(first*stack.pop())
                print(stack)
            elif char == '/':
                first = stack.pop()
                stack.append(int(stack.pop()/first))
                print(stack)
            else:
                stack.append(int(char))
                print(stack)
        print(stack)
        return stack[-1]


        