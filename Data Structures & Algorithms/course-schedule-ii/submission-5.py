class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dd = defaultdict(list)
        pre,n = prerequisites,numCourses
        visited , taken, res = set(), set(),[]
        for cour,prereq in pre:
            dd[cour].append(prereq)

        def dfs(c):
            if c in visited:
                return False
            if c in taken:
                return True
            
            visited.add(c)
            #subres = []
            for p in dd[c]:
                if dfs(p) == False:
                    return False
            #    else: subres.appendd(p)
            visited.remove(c)
            #dd[c] == []
            taken.add(c)
            res.append(c)
            #res.update(list(subres)[::-1])
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        #    else: res.append(i)
        return list(res)
           

