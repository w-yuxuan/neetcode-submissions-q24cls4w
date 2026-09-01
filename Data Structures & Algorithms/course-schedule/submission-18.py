class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        n = numCourses
        mem = defaultdict(list)
        for c,p in pre:
            mem[c].append(p)

        visit ,safe = set(),set()
        
        def dfs(i):
            if i in visit:
                return True
            if i in safe:
                return False
            visit.add(i)
            for j in mem[i]:
                if dfs(j):
                    return True
            visit.discard(i)
            safe.add(i)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
