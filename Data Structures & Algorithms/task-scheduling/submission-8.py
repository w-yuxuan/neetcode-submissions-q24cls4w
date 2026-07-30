class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mem = Counter(tasks)
        #h = list(mem.values()) # 
        h=[-v for v in mem.values()]
        heapq.heapify(h)
        q = deque()
        time = 0

        while h or q:
            time +=1
            if q:
                n2,v2 = q[0]
                if time >= n2:
                    heapq.heappush(h,v2)
                    q.popleft()
            if h:
                v1=heapq.heappop(h)
                if v1+1<0:
                    q.append([n+time+1,v1+1])
        return time 
                

