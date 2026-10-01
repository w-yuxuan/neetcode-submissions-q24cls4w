class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
       n=len(tasks)
       for i in range(n):
            tasks[i].append(i)
       tasks.sort(key=lambda x:x[0])
       tasks = deque(tasks)
       res = []
       ready = []
       heapq.heapify(ready)
       t=tasks[0][0]
       while ready or tasks:

            while tasks and tasks[0][0]<=t:
                q,p,i = tasks.popleft()
                heapq.heappush(ready,(p,i))
            if not ready: # only possible when tasks[0][0]>t, we skip to that time
                t=tasks[0][0]
                continue # so that we get a chance to pop that right away to see if we can now have anything ready to be process
            # use it 
            p1,i1 = heapq.heappop(ready)
            t+=p1
            res.append(i1)
       return res

         