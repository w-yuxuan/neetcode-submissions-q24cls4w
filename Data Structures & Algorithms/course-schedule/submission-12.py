class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nc,pre = numCourses,prerequisites
        mem = defaultdict(list)
        for cour,req in pre:
            mem[cour].append(req)
        safe = set()
        visit= set()

        def check(c):
            #edge cases
            if c in safe:
                return True
            if c in visit:
                return False
            visit.add(c)
            for i in mem[c]:
                if not check(i) :
                    return False
            visit.discard(c)
            safe.add(c)
            return True

        for cl in range(nc):
            if cl not in safe:
                if not check(cl):
                    return False
        
        return True


            
