class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        def dfs(i,j): # j is largest index I chose, i is starting index
        # return so far how long the longest is 
            
            if i==len(nums):
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]

            # longest = 0
            # for k in range(i+1,len(s)):
            #     if nums[k]> nums[j]:
            #         longest = k-

            # if i+1 <= len(nums)-1: #have right neighbor
            
            if nums[i]> nums[j] or j==-1: # current site is the new largest site
            # 2 branches: if i should keep it 
                mem[(i,j)] = max(dfs(i+1,j),dfs(i+1,i)+1)
                return mem[(i,j)] 
            else:
                mem[(i,j)] = dfs(i+1,j)
                return  mem[(i,j)] 
                
        return dfs(0,-1)

            


