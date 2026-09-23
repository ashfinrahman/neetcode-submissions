class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Index2 - Index1 = length
        #height = lowestIndexHeight
        #Two pointers
        #Move the lower height pointer in each iteration
        #Calculate the volume and compare with current max
        #return current max
        currMax = -1
        l = 0
        r = len(heights)-1

        while l < r:
            width = r - l
            if heights[l] > heights[r]:
                length = heights[r]
            else:
                length = heights[l]

            if currMax < length*width:
                currMax = length*width
            
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
            
        return currMax



