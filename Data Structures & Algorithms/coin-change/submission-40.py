class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [-1]*(amount+1)
        def dfs(tot):
            if tot == amount:
                return 0
            if tot > amount:
                return float('inf')
            if mem[tot] != -1:
                return mem[tot]

            cur = float('inf')
            for c in coins:
                cur = min(cur,dfs(tot+c)+1)
            mem[tot] = cur
            return cur

        return dfs(0) if dfs(0)!=float('inf') else -1


