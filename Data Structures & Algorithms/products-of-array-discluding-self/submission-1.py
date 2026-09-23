class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        #nums = [1,2,4,6]
        #output=[0,0,0,0]
        j=0
        for i in range(len(nums)):
            j += 1
            for j in range(len(nums)-1):
                past = output[i]
                mult = nums[(j+(i+1))%len(nums)]
                output[i] = past*mult
                print(mult)
        return output

            