class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        new,res = [],[]
        for i in range(n):
            tasks[i].append(i)
            new.append(tasks[i])
        tasks = sorted(new, key = lambda x: x[0])
        tasks = deque(tasks)
        t = tasks[0][0]
        ready , wait = [],[]
        heapq.heapify(ready)
        # heapq.heapify(wait)
        # q,p,i = tasks.popleft()
        # t = q
        # heapq.heappush(ready,(p,i))

        while ready or tasks: # process 1 task
            #in case there are gaps betw tasks
            if not ready:
                t = max(t,tasks[0][0])

            while tasks and tasks[0][0] <= t: # move tasks that you can process to ready
                q1,p1,i1 = tasks.popleft()
                heapq.heappush(ready,(p1,i1))
            
            # either there are tasks ready, or there were tasks in the beginning that just got added to ready
            p,i = heapq.heappop(ready)
            t += p # process it
            res.append(i)

        return res
        
