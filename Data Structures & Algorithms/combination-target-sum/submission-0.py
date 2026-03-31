class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort it and do it like a 2sum question nlogn: remembr to check duplicat combin
        # naiive: check for all pairs, triples ... cost for pairs is n^2, triples are n^3
        #do combinations and then check for sum = target : n!(n-k)!/k! : order n^2 lower than k*2^n
        cur,res = [], []
        def dfs(i,cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return # end the search on this branch
            if sum(cur) > target:
                return
            # if i > len(nums)-1:
            #     return

            for j in range(i,len(nums)):
                cur.append(nums[j])
                dfs(j,cur)
                cur.pop()
                
        dfs(0,cur)
        return res


