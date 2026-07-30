class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    # 0 case ? 
        mem = [0]*(amount+1)
        mem[amount]=1
        # for j in mem.reverse() :
        for i,c in enumerate(coins):
            for j in range(amount,-1,-1) :            
                # if c+j ==amount:
                #     mem[c+j] += mem[j]
                if c+j <= amount and mem[c+j]!=0:
                    mem[j] += mem[c+j]
        
        return mem[0]

        # def dfs(tot):
        #     if tot > amount:
        #         return 0
        #     if tot == amount:
        #         return 1
        #     way = 0