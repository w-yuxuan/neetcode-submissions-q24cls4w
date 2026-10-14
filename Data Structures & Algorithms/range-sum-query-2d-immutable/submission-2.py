class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROW,self.COL = len(matrix),len(matrix[0])
        self.row,self.col = self.ROW-1,self.COL-1
        self.matrix = matrix
        tot = 0
        self.mem = {}
        for m in range(self.ROW):
            for n in range(self.COL):
                self.mem[(m,n)] = tot
                tot+=matrix[m][n]
        self.tot = tot

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1,row2+1):
            if col2+1 <= self.col:
                res+= self.mem[(i,col2+1)] - self.mem[(i,col1)]
            else: # go to next line
                if i < self.row: #not last row
                    res+= self.mem[(i+1,0)] - self.mem[(i,col1)]
                else: # last row
                    res+= self.tot - self.mem[(i,col1)]
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)