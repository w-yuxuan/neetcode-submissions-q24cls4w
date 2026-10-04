class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n==1:
            return 1
        l,r = 0,n-1
        res = 0
        p = people

        # sorted(people,key = lambda x:-x) # max at the top
        people.sort()
        people.reverse()

        while 0<=l <= r <n:
            if p[l]+p[r] > limit:
                l+=1
            else:
                l+=1
                r-=1
            res+=1
        return res
