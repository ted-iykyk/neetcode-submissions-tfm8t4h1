class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # find the corner

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if row == row1 and col == col1:
                    res = 0
                    i, j = 0, 0
                    xboundry = col2 - col #5-3 = 2
                    yboundry = row2 - row #5-4 = 1
                    print(yboundry)
                    for i in range(yboundry + 1):
                        for j in range(xboundry + 1):

                            res += self.matrix[row + i][col + j]
                    return res

        return 0
                    



# row1 = 2, col1 = 1 -- row2 = 4, col2 = 3
# [3, 0, 1, 4, 2] 
# [5, 6, 3, 2, 1] 
# [1, 2, 0, 1, 5] 
# [4, 1, 0, 1, 7]
# [1, 0, 3, 0, 5]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)