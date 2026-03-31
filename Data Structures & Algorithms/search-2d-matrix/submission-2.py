class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0 #m comparisions in the first col
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                r=i
            else: 
                r=i-1 # found the row
                break
        
        # if len(matrix)-1<=0:
        #     return False
        
        # if matrix[r+1][0] == target:
        #     return True
        
        #if r==0:return False
        line = matrix[r]
        def search(lst):               #??
            if not lst:
                return False
            mid = len(lst)//2
            if target == lst[mid]: return True
            elif target < lst[mid]:
                return search(lst[:mid])
            else:
                # if len(lst)==1: return False
                return search(lst[mid+1:])

        return search(line)==True
        #check single element case


        