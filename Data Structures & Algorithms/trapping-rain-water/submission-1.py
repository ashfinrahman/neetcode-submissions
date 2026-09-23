class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
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
