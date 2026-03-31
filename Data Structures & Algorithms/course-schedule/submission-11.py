class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre= prerequisites
        nc = numCourses 
        #detect loop
        visit = set()
        safe = set()
        mem = defaultdict(list)

        for c,p in pre:
            mem[c].append(p)

        def find(c):
            if c in safe:
                return True
            elif c in visit:
                return False
            #try starting from c
            visit.add(c)
            for p in mem[c]:
                if find(p) == False:
                    return False
            visit.discard(c)
            safe.add(c)

        for c in range(nc):
            if find(c) == False:
                return False
        
        return True

            

            




    
