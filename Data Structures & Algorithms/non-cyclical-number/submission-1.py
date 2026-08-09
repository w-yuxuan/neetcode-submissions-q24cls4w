class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def dfs(n):
            if n == 1:
                return True
            if n in visit:
                return False

            # Add 'n' (the current state) to visit BEFORE moving forward
            visit.add(n)

            # Sum squared digits dynamically for numbers of ANY length
            res = sum(int(d) ** 2 for d in str(n))

            return dfs(res)

        return dfs(n)