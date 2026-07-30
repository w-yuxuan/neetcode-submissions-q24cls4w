class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i,j): # returns largest so far , i is starting index, j is index of largest
            
            if (i,j) in mem:
                return mem[(i,j)]
            if i>len(nums)-1:
                return 0
            if j==-1 or nums[i]>nums[j] :
                mem[(i,j)] = max(dfs(i+1,j),dfs(i+1,i)+1)
            else:
                mem[(i,j)] = dfs(i+1,j)

            return mem[(i,j)]
        return dfs(0,-1)
