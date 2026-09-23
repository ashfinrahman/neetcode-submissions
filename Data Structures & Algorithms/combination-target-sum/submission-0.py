class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def bt_dfs(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    continue
                path.append(nums[i])
                bt_dfs(i, remaining - nums[i])   # i, not i+1 — reuse allowed
                path.pop()

        bt_dfs(0, target)
        return result