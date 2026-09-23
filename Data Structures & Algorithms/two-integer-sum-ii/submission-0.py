class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force, compare each with each with 2 pointers
        l = 0
        r = len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l+1, r+1]
            elif curSum > target:
                 r-=1
            elif curSum < target:
                l +=1 
        return []
        