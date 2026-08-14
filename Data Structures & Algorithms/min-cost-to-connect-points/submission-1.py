import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # 1. Build adjacency list with Manhattan distance using node indices
        mem = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # Manhattan distance: |x1 - x2| + |y1 - y2|
                d = abs(x1 - x2) + abs(y1 - y2)
                mem[i].append((d, j))
                mem[j].append((d, i))
        
        # 2. Prim's Algorithm
        visited = set()
        min_heap = [(0, 0)]  # (cost, node_index)
        total_cost = 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            
            if u in visited:
                continue
                
            visited.add(u)
            total_cost += cost
            
            for d, neighbor in mem[u]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (d, neighbor))
                    
        return total_cost