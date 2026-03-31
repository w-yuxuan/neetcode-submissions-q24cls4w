class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        cur = []
        res = []
        def find(i,total):
            if total==target:
                res.append(cur.copy())
                return
            if i > len(nums)-1 or total>target:
                return
            
            #include current
            cur.append(nums[i])
            find(i+1,total+nums[i])
            cur.pop()

            #exclude current
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            find(i+1,total)
        find(0,0)
        return res