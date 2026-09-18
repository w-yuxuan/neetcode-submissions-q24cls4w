class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[int]:

        if n == 1:
            return [0]

        nei = defaultdict(list)
        cnt = {node: 0 for node in range(n)}

        for a, b in edges:
            cnt[a] += 1
            cnt[b] += 1
            nei[a].append(b)
            nei[b].append(a)

        while len(cnt) > 2:
            # First, identify the complete current layer.
            layer = []

            for node, links in cnt.items():
                if links == 1:
                    layer.append(node)

            # Then remove that entire layer.
            for node in layer:
                for neighbor in nei[node]:
                    if neighbor in cnt:
                        cnt[neighbor] -= 1

            for node in layer:
                cnt.pop(node)

        return list(cnt.keys())