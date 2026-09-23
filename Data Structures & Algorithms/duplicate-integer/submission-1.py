class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        #can use if x in set{} then return true
        for i in range(len(nums)):
            if nums[i] in newSet:
                return True
            else:
                newSet.add(nums[i])
        return False
        
        