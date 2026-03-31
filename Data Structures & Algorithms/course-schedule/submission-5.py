class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        # initialize
        conn = defaultdict(list)
        pre, num = prerequisites, numCourses
        need = set()

        # build dict
        for cour, prereq in pre:
            conn[cour].append(prereq)
            
        # def dfs recursion call to mimic going down a path;
        def dfs(c):   
            if not conn[c]: # easiest True
                return True
            if c in need: # easiest False
                return False 

            need.add(c)
            for p in conn[c]: # help check further levels down this path
                     # scans the branches originated from p
                if dfs(p) == False:
                    return False
            need.remove(c) # pop it after scans the branches originated from p
            return True

        # for loop to use dfs: 
        # Using list(conn) prevents RuntimeError when defaultdict adds keys during recursion
        for course in list(conn): 
            if not dfs(course): return False
            
        return True