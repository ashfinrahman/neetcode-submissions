class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        currMax = 0
        stack = [] # [temp, index]
        returns = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                returns[stackInd] = i - stackInd
            stack.append([t, i])
        return returns

