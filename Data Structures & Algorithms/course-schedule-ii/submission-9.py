class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = prerequisites
        res = []

        def dfs(c): # check if there is a cycle, returns False if found one. 
            #base
            if c in need:
                return False
            if c in taken:
                return True
            
            #start search for loops
            need.add(c)
            for p in mem[c]:
                if dfs(p) == False:
                    return False
            need.remove(c)
            taken.add(c)
            res.append(c)
            return True

        
        mem = defaultdict(list)
        taken = set()
        need = set()
        
        for course,prereq in pre:
            mem[course].append(prereq)
        for course in range(numCourses):
            
            if dfs(course) == False:
                return []
        return res

