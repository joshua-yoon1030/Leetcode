#print a 90 degree rotation of a matrix
#https://leetcode.com/problems/rotate-image/
#my strategy: rotate groups of 4 blocks at a time in a 90 deg circle
#a better strategy: reflect along diagonal, and then reverse the matrix.
#runtime: O(n^2) because we change every element of the matrix at most once.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 1
        #don't forget to bound your loops correctly! Huge errors here.
        for row in range(n//2):
            for col in range(row, n-row-1):
                #a = top left
                #b = top right
                #c = bottom right
                #d = bottom left 
                a = matrix[row][col]
                b = matrix[col][n-1-row]
                c = matrix[n-1-row][n-1-col]
                d = matrix[n-1-col][row]

                matrix[row][col] = d
                matrix[col][n-1-row] = a
                matrix[n-1-row][n-1-col] = b
                matrix[n-1-col][row] = c

                