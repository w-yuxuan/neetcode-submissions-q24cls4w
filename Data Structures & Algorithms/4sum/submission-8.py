class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        def two(l,t):
            r = n-1
            res1 = []
            while l<r:
                cur = nums[l]+nums[r]
                if cur > t:
                    r-=1
                elif cur < t:
                    l+=1 
                else:
                    res1.append([nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l<r and nums[l] == nums[l-1]: 
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
            return res1
            
        def dfs(k,st,tot):
            res2 = []
            if k==2:
                return two(st,tot)
            for i in range(st,n):
                if i>st and nums[i]==nums[i-1]:
                    continue
                temp = dfs(k-1,i+1,tot-nums[i])
                if temp:
                    for lst in temp:
                        res2.append([nums[i]]+lst)
            return res2
        return dfs(4,0,target)
                


