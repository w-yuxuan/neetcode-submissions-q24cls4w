class Solution:
    def jump(self, nums: List[int]) -> int:
        # start from the right 
        mem = [float('inf')]*len(nums)

        if len(nums)==1:
            return 0
        mem[-1]=0
             
        # reverse interate one by one for bottom up: not recursive but iter
        for i in range(len(nums)-1,-1,-1): 
            maxjump=min(len(nums)-1,i+nums[i])
            for j in range(i+1,maxjump+1): #can reach i from j
                mem[i]=min(mem[j]+1,mem[i])
                # j-=1
        return mem[0]    

                



        # def df(i): #return min num steps so far 
            
        #     return
        # return df(0)