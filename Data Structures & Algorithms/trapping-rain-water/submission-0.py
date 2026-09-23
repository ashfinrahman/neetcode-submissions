class Solution:
    def trap(self, height: List[int]) -> int:
    #height = [0,2,0,3,1,0,1,3,2,1]
    #prefix = [0,2,2,2,3,3,3,3,3,3] 
    #suffix = [3,3,3,3,3,3,3,3,2,1]
    #min(prefix[l], suffix[r]) - height[i]

        prefix = [0]*len(height)
        suffix = [0]*len(height)
        l = 0
        r = len(height) - 1
        runningHeight = 0
        for i in range(len(height)):
            if runningHeight < height[i]:
                runningHeight = height[i]
            prefix[i] = runningHeight
        runningHeight = 0
        for i in range(len(height)):
            if runningHeight < height[len(height) - 1- i]:
                runningHeight = height[len(height) - 1 - i]
            suffix[len(height) - 1 - i] = runningHeight
        print(prefix, suffix)

        counter = 0
        for i in range(len(height)):
            counter += min(prefix[i], suffix[i]) - height[i]
        return counter
