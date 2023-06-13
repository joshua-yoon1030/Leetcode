class Solution:
    def restoreMatrix(self, rowSum, colSum):
        matrix = [[0 for j in range(len(colSum))] for i in range(len(rowSum))]

        isDone = False

        while(not isDone):
            isDone = True
            
            rowInd, row = min(enumerate(rowSum), key = lambda x: x[1] if x[1]> 0 else float('inf'))
            colInd, col = min(enumerate(colSum), key = lambda x: x[1] if x[1]> 0 else float('inf'))
            
            if row == float('inf'):
                continue

            isDone = False
            minimum = min(row, col)

            matrix[rowInd][colInd] = minimum
            rowSum[rowInd] -= minimum
            colSum[colInd] -= minimum
        return matrix
