class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        res.append(nums[0])
        i = 0
        while i < len(nums):
            if nums[i] != res[-1]:
                res.append(nums[i])
            i += 1
        nums[:len(res)] = res
        return len(res)
            