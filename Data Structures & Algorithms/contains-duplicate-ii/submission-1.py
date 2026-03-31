class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

#prev err: tried to keep R from going too far from L, and moving L by 1 each 
# time the R "for loop" , but that req another for loop
# here we only move R and use the k condition instead as a signal to start moving L

        for R in range(len(nums)):
            if R - L > k: # False if R=L. It will move R if still possible to keep going
                window.remove(nums[L]) 
                L +=1
            #do the previous line to check before I decide if the current steps returns T
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False