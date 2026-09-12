class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res2 = []
        def dfs(st,tot):
            res1= []
            for i in range(st,n):
                l,r= i+1,n-1
                t = tot-nums[i]
                # if i>st and nums[i] == nums[i-1]:
                #     continue
                while l<r:
                    if nums[l]+nums[r] > t :
                        r-=1
                    elif nums[l]+nums[r] == t:
                        res1.append([nums[l], nums[r], nums[i]])
                        r-=1
                        l+=1
                        # while l<r and nums[l]==nums[l-1]:
                        #     l+=1
                        # while l<r and nums[r] == nums[r+1]:
                        #     r-=1
                    else:
                        # while nums[l]==nums[l-1]:
                        l+=1
            return res1

        for j in range(len(nums)-3):
            # if j>0 and nums[j]==nums[j-1]:
            #     continue
            temp = dfs(j+1,target-nums[j])

            for triplets in temp:
                h = [nums[j]]
                h.extend(triplets)
                if h not in res2:
                    res2.append(h)

        return res2
