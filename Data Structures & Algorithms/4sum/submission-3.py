class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        def two(l,r,t):
            res1 = []
            while l<r:
                if nums[l]+nums[r] > t:
                    r-=1
                elif nums[l]+nums[r] == t: 
                    res1.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                else:
                    l+=1
            return res1
        
        def dfs(st,t,k):
            # for kth in range(k+1-):
            if k==2:
                return two(st,n-1,t)
#for each prob, i take an item and use the following string to solve the k-1 level problem get its result, and add my item into it
            res2 = []
            for i in range(st,n):
                temp = dfs(i+1,t-nums[i],k-1)
                if temp:
                    for item in temp: # items is one of the list that satisfy req
                        if item+[nums[i]] not in res2: # check duplicates. we sort nums so if there is a repeat, it has to follow order [temp,nums[i]]
                            res2.append(item+[nums[i]])
            return res2

        return dfs(0,target,4)
                    



