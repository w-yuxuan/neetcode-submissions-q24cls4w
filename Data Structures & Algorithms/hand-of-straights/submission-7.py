class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mem = Counter(hand)
        lst = sorted(mem.keys())
        rank = deque(lst)

        while mem.keys():# start a new group
            v = rank[0]

            for i in range(groupSize):
                if rank == []:
                    return False
                if v+i not in mem:
                    return False

                mem[v+i]-=1
                if mem[v+i]<=0:
                    mem.pop(v+i)
                    rank.remove(v+i)
        return True

