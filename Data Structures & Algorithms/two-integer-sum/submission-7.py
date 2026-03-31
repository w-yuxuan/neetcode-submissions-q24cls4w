class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for j, i in enumerate(nums):
            find = target - i
            if find in h: # O(n)
                return [h[find],j]
            h[i]=j