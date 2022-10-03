class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefixSum = [[0 for col in range(len(matrix[0]))]for row in range(len(matrix))]
        self.prefixSum[0] = matrix[0]
        for i in range(1, len(matrix)):
            self.prefixSum[i] = [a + b for a,b in zip(self.prefixSum[i-1], matrix[i])]
        print(self.prefixSum)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        prefixRow = [0] * len(self.prefixSum[0])
        for i in range(len(self.prefixSum[0])):
            if row1!= 0:
                prefixRow[i] = self.prefixSum[row2][i] - self.prefixSum[row1-1][i]
            else:
                prefixRow[i] = self.prefixSum[row2][i]
        sum = 0
        for i in range(col1, col2+1):
            sum += prefixRow[i]
        return sum
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

mySol = NumMatrix([[1,1,1],[1,1,1], [1,1,1]])
print(mySol.sumRegion(0,0,2,2))