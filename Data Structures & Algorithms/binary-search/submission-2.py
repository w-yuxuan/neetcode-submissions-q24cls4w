class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find(sublist,target):
            pt = len(sublist)//2
            if sublist[pt] == target:
                return pt
            if len(sublist) ==1:
                return float('inf')
            elif sublist[pt] > target:
                return find(sublist[:pt],target)
            else: 
                return find(sublist[pt:],target)+pt
        if find(nums,target) != float('inf'):
            return find(nums,target)
        else: return -1