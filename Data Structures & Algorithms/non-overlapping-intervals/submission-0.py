class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        lst = sorted(intervals,key=lambda x: x[1] )
    
        res = -1
        cur = lst[0]
        for s,e in lst:
            if s < cur[1]:# overlap
                res +=1
            else: 
                cur = [s,e]
        return res

            # no need to check if new commer ends at the same spots and start earlier than prev interval. in that case we still delete the new one

                # if e == cur[1] and s < cur[0]:
                #     cur = 
                




