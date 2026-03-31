class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        if len(stones) == 1: return stones[0] * -1
        elif len(stones) == 0: return 0
        
        heapq.heapify(stones)
        #after you heapify you turn list to heap in place
        #h = heapq.heapify(stones)
       # twoStones = heapq.nsmallest(2,stones)
        #better than heap only if n is small like 2


        while True:
        #if twoStones[0] = twoStones[1]:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
 
            if second > first:
                add = second - first
                heapq.heappush(stones,-1*add)
             
            if len(stones) == 1: return stones[0] * -1
            elif len(stones) == 0: return 0