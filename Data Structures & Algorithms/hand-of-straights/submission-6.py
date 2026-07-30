# counter way
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        countd=Counter(hand)
        lst = list(countd.keys())
        val = deque(sorted(lst))
        while countd.keys():
            v = val[0]
            for i in range(groupSize):
                if v not in countd:
                    return False
                countd[v]-=1
                if countd[v]<=0:
                    countd.pop(v)
                    val.remove(v)
                v+=1
        return True
