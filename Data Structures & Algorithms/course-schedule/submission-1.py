class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        conn = defaultdict(list)
        taken = 0
        #level = 0 #num levels of prereq we did
        pre = prerequisites
        n = numCourses

        deg = [0]*n
        # i can keep doing dfs to see if I find a way to reach taken==numCourses
        
        #build graph, reverse to {class:next can take}

        for cour,prereq in pre:
            conn[prereq].append(cour)
            deg[cour]+=1

        visit = set()        
        q = deque()
        #q.append(0)  to avoid error for [[0,1]], append one that must exist
        for it in range(n):
            if deg[it] == 0:
                q.append(it)
                visit.add(it)

        #start traversing from 0 as it must be present
        while q:
            pop = q.popleft()
            taken+=1

            #no need to check out of bdry or hindering 1s, check if visited
            #if not conn[pop]: # if no prereq, already added to visit and just got poped from q, for loop below works
            for j in conn[pop]: #prereqs 1by1
                if j not in visit:
                    deg[j]-=1

                if deg[j] == 0 :
                    q.append(j)
                    visit.add(j)
                
        return taken == n


        