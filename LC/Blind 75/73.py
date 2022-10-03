class Solution(object):
    def mark(self, matrix, i, j):
        for x in range(len(matrix)):
            matrix[x][j] = 0.5 #nonsensical value for integer matrix
        for y in range(len(matrix[i])):
            matrix[i][y] = 0.5
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    print(i, j)
                    self.mark(matrix, i, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0.5:
                    matrix[i][j] = 0