class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in {"+", "-", "*", "/"}:
                stack.append(int(val))
            elif (val == "+"):
                second = stack.pop()
                first = stack.pop()
                stack.append(first+second)
            elif(val == "-"):
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            elif (val == "*"):
                second = stack.pop()
                first = stack.pop()
                stack.append(first*second)
            elif (val == "/"):
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second))
        return stack[0]   

