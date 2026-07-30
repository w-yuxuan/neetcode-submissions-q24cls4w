class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        dp = defaultdict(list)

        for c,p in pre:
            dp[c].append(p)

        visit = set()
        safe = set()
        
        def dfs(i):
            if i in safe:
                return True
            if i in visit:
                return False
            visit.add(i)
            for j in dp[i]:
                if not dfs(j):
                    return False
            visit.discard(i)
            safe.add(i)
            return True
        
        for n in range(numCourses):
            if n not in safe:
                if not dfs(n):
                    return False
        return True