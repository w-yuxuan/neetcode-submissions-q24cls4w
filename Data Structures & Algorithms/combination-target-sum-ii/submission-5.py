class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        nums.sort()
        res = []
        cur = []
        def dfs(i):
            if sum(cur) == target: ############
                res.append((cur.copy()))
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
            nxt = i+1
            while nxt<=len(nums)-1 and nums[nxt]==nums[nxt-1] :
                nxt+=1
            dfs(nxt)
#            cur.pop()
        dfs(0) ############
        return res

# what we are trying to avoid is that 113, the first 1 can choose to take another 1 or not take the 1 and move to 2nd 1.
# if we move onto the second 1 without taking the first, we don't want it to take 

