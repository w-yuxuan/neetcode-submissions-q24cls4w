class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        def dfs(n):
            if n in visit:
                return False
                
            visit.add(n)
            # thou = (n//1000)%10
            # hund  = (n//100)%10
            # ten =  (n//10)%10
            # one = n %10
            
            res = sum(int(d)**2 for d in str(n))
            if res ==1:
                return True
            return dfs(res)

        return dfs(n)