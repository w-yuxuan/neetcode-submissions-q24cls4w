class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre= prerequisites
        nc = numCourses 
        mem = defaultdict(list)
        for cour,prereq in pre:
            mem[cour].append(prereq)
        res = []
        taken = set()
        visit = set() # what i'm visiting in the loop
        #detect loop
        def check(c):
            if c in taken:
                return True
            elif c in visit:
                return False
            
            visit.add(c)
            for i in mem[c]:
                if check(i)==False:
                    return False       
            taken.add(c)
            visit.remove(c)
            res.append(c)
            #don't remove it from visit bc now it's part of our path
            return True

        for c in range(nc):
            if check(c) == False:
                 return []

        return res
            