class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        results = []
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        print(map.values())
        for _ in range(k):
            maxi = -1
            maxnum = nums[0]
            for num, freq in map.items():
                if max(maxi, freq) == freq:
                    maxi = freq
                    maxnum = num
            results.append(maxnum)
            map.pop(maxnum)
        return results
                    



