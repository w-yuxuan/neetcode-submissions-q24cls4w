class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # plan: heapify the ord(tasks), if the one you just popped is the same index as last one, add n to your steps 
        
        # mem = {}
        # for t  in tasks:
        #     mem[t] = mem.get(t,0)+1
        
        count = Counter(tasks)
        mem = [cnt for cnt in count.values()]

        heapq.heapify_max(mem)
        q = deque()
        t=0
        while mem or q:
            t+=1
            ################## key notice: not top = mem.pop()
            if mem: # don't forget so next line won't be error
                top= heapq.heappop_max(mem)
                if top-1:
                    q.append((top-1,t+n))
            if q and q[0][1] ==t:
                ################## key notice: not mem.heappush_max(q[0][0]) ##################
                heapq.heappush_max(mem,q[0][0])
                q.popleft()
        return t
        