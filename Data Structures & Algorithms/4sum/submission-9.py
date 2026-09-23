class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        def two(i,tot):
            l,r = i, n-1
            res2 = []
            while l<r:
                if nums[l]+nums[r]==tot:
                    res2.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r] > tot:
                    r-=1
                else:
                    l+=1            
            return res2

        def find(k,start,tot):
            final = []
            if k==2:
                return two(start,tot)
            for st in range(start,n):
                if st > start and nums[st] == nums[st-1]:
                    continue
                cur = find(k-1,st+1,tot-nums[st])
                if cur:
                    for grp in cur:
                        temp = []
                        temp.append(nums[st])
                        temp.extend(grp)
                        final.append(temp)
                # for j in range(st,n)
            return final

        return find(4,0,target)
