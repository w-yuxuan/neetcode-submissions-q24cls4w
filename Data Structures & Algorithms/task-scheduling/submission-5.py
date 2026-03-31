class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # do the most frequent tasks first , count with a mem
        mem = {}
        time = 0
        q = deque()
        # one task check

        for t in tasks:
            # mem[t].append(tasks.pop())
            mem[t] = mem.get(t,0)+1

        # if use heap to store o(n) to create, nlogn to pop all
        # if use list, then n log n to store, O(n) to pop
        rank = []
        for t in mem:
            rank.append((-mem[t],t,0)) #(need_to_repeat#,task,when_can_next)
        heapq.heapify(rank)

        # one = rank[0][0]
        while q or rank: #pop from rank, add to q, check if q[0] can be processed
            time +=1            
            if rank:
                check = list(heapq.heappop(rank))
                if check[0] <-1:
                    check[0] += 1
                    check[2] = time+n
                    q.append(tuple(check))
            if q and q[0][2] <= time:
                nxt = q.popleft()
                heapq.heappush(rank,nxt)
        return time

            
            

        

