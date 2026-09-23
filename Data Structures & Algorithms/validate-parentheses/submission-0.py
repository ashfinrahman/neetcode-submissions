class Solution:
    def isValid(self, s: str) -> bool:
        #push open brackets and pop to check if top matches close bracket
        stack = []
        for char in s:
            match char:
                case '(':
                    stack.append(char)
                case '{':
                    stack.append(char)
                case '[':
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
        return len(stack) == 0