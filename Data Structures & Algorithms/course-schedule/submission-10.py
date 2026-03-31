class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre= prerequisites
        nc = numCourses 
        # look for circles 
        # as long as the course has prereq: do dfs on it to check if it has circular prereq
        # if it doesn't have, mark it as taken
        # for all the prereq on a dfs branch, mark it as needed
        #bfs: return courses with least num prereq first
        #dfs: 


        def dfs(need,c):
 
            #base cases
            if c in need:
                return False
            if c in taken:
                return True
            
            need.add(c)
            for p in mem[c]:
                #need.add(p)
                if dfs(need,p) == False:
                    return False
                #need.remove(p)
            need.remove(c)
            taken.add(c)
            return True

        taken = set()
        mem = defaultdict(list)
        for course,prereq in pre:
            # build a hash for (course,prereq)?
            # sure, at most i traverse the whole prereq list an extra time
            mem[course].append(prereq)

            # check if no prereq by seeing if its val is none
        for course in range(numCourses):
            need = set()
            if mem[course] == []:
                taken.add(course)
            if dfs(need,course) == False:
                return False

        return True
            
            

            




    
