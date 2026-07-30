from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        nc = numCourses
        req = defaultdict(list)
        safe = set()
        path = []
        res = []

        for c, p in pre:
            req[c].append(p)

        def check(c):
            if c in safe:
                return True
            if c in path:
                return False
            path.append(c)    
            for p in req[c]:
                if not check(p):return False
                # return False if not check(p)
            path.pop()
            return True
        
        for c in range(nc):
            if c not in safe:
                if not check(c):
                    return False
        return True

        
