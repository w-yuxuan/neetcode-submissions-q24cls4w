class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dd = defaultdict(list)
        pre,n = prerequisites,numCourses
        visited = set()
        for cour,prereq in pre:
            dd[cour].append(prereq)

        def dfs(c):
            if c in visited:
                return False
            if dd[c] == []:
                return True
            
            visited.add(c)
            for p in dd[c]:
                if dfs(p) == False:
                    return False
            visited.remove(c)
            dd[c] == []
            return True
        
        for i in range(numCourses):
            if dd[i] != []:
                if dfs(i) == False:
                    return False
        return True
            

