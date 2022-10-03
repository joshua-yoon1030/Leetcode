class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)#rows
        n = len(obstacleGrid[0])#cols
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        #first make our answer matrix and pad the bottomrow/right col with 0s
        matrix = [ [0]*(n+1) for _ in range(m+1) ]
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if(x == m-1 and y == n-1):
                    #first square is always 1
                    matrix[m-1][n-1] = 1
                elif(obstacleGrid[x][y] == 1):
                    #on an obstacle
                    matrix[x][y] = 0
                else:
                    #default, count paths
                    matrix[x][y] = matrix[x+1][y] + matrix[x][y+1]
        return matrix[0][0]        

#mySol = Solution()
#print(mySol.uniquePathsWithObstacles([[0,0],[1,1], [0,0]]))