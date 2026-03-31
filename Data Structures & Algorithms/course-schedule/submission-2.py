class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        prereq=prerequisites

        taken = 0
        conn = defaultdict(list) #course to prereq
        deg = [0]*n
        q = deque()
        #visit no need, and starting cell is always good 
        for cour, prereq in prerequisites:
            conn[prereq].append(cour)
            deg[cour]+=1

        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        while q:
            # no need to check stopping condi
            p = q.popleft()
            taken +=1
            for pre in conn[p]:
                deg[pre]-=1
                if deg[pre] ==0:
                    q.append(pre)
        return taken == n




