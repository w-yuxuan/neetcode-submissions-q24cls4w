class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i):
            if sum(cur) == target: ############
                res.append(cur.copy())
                return
            if  sum(cur)>target or i>len(nums)-1:
                return
                ###########
        
            #with current
            cur.append(nums[i]) ############
            dfs(i)
            cur.pop()

            
            # without current
#            cur.append(nums[i+1])
            dfs(i+1)
#            cur.pop()
        dfs(0) ############
        return res