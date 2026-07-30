class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # puttin in the largest values first don't 
        # necessarily make you need less coins to fill the tot
        mem= [-1]*(amount+1)

        def dfs(tot): # min coins needed to get to tot
            if tot==0:
                return 0 

            # if tot==amount:
            #     return 1
            
            # if tot>amount:
            #     return float('inf')



            if tot<0:
                return float('inf')

            if mem[tot]!=-1:
                return mem[tot]

            res = float('inf')
            for c in coins:
                res = min(dfs(tot-c)+1,res)

            mem[tot] = res
            return mem[tot]

        
        return dfs(amount) if dfs(amount)!=float('inf') else -1
            

            

                
            