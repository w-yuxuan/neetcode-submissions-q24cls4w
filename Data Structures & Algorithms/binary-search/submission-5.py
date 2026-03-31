class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(sublist,target):
            pt = len(sublist)//2
            if sublist[pt] == target:
                return pt
            if len(sublist) == 1:
                return -1
            elif sublist[pt] > target:
                return find(sublist[:pt],target)
            else: 
                x=find(sublist[pt:],target)
                if x == -1:
                    return -1
                else: 
                    return x+pt
        return find(nums,target)
        