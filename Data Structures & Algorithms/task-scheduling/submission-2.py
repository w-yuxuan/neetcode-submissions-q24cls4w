class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mem = [-cnt for cnt in count.values()]

        q= deque()
        heapq.heapify(mem)
        t=0
        while q or mem: #q = [cnt,time to activate]
            t+=1
            if mem:
                cnt = heapq.heappop(mem)+1
                if cnt < 0:
                    q.append((cnt,t+n))
            if q:
                if t == q[0][1]:
                    heapq.heappush(mem,q.popleft()[0])
        return t
