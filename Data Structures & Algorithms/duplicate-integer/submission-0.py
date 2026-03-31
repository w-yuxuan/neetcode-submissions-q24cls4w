class Solution:
    def hasDuplicate(self, nums):
        saw=set()
        for i,n in enumerate (nums):
            
            if n in saw:
                return True
            else: saw.add(n)

        return False

    
            
