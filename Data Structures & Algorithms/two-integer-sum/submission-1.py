class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make key target-nums[i]
        newDict = {}
        for i in range(len(nums)):
            if target-nums[i] in newDict:
                return [newDict.get(target-nums[i]), i]
            else: 
                newDict[nums[i]] = i
                