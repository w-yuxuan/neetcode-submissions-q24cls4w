class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        mem = defaultdict(list)

        for c,p in pre:
            mem[c].append(p)
        
        visit = set()
        safe = set()

        def dfs(n): # check the next node can be traversed?
            if n in visit:
                return False
            
            if n in safe:
                return True
            
            visit.add(n)
            for pr in mem[n]:
                if not dfs(pr):
                    return False
            
            visit.discard(n)
            safe.add(n)
            return True
        
        for n in range(numCourses):
            if n not in safe and dfs(n)==False:
                return False 
        
        return True





