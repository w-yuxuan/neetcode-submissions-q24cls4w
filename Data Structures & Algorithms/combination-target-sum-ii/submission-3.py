class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        nums.sort()
        res = set()
        cur = []
        def dfs(i):
            if sum(cur) == target: ############
                res.add(tuple(cur))
                return
            if  sum(cur)>target or i>len(nums)-1 :
                return
                ###########
        
            #with current
            cur.append(nums[i]) ############
            dfs(i+1)
            cur.pop()

            
            # without current
#            cur.append(nums[i+1])
            dfs(i+1)
#            cur.pop()
        dfs(0) ############
        return [list(i) for i in res]