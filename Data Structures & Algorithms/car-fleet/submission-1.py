class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # each loop is each time step
        #keep updating the current positions, if I passed them then floor it back
        # O((target-minPos)/minspeed)
        # can't sort this: else i mess up the order of the speed
        time = []
        for i in range(len(speed)):
            time.append(((target-position[i])/speed[i]))
        lst = [(position[i],time[i]) for i in range(len(time))]
        srt = sorted(lst,key=lambda x: x[0]) #,reverse = True)

        s = []
        while srt:
            x,t = srt.pop()
            if not s or t > s[-1][1]:
                s.append((x,t))
            # <= case: since we only care about t, no need to do anything
        return len(s)










