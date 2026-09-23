class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # map them all to a map
        #value should be target - num
        #iterate over map, for each num search

        #Two Pointer approach
        #Right Pointer: If num is larger than target, continue
        # if right + left > target right++
        #if right + left < target left++
        #if right + left == target return [left + right]

        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]