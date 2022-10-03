#print the matrix in spiral order:
#I just implemented it by following the steps, just making sure it's not empty.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        while matrix:
            ans = ans + matrix.pop(0)
            if not matrix:
                continue
            for i in range(len(matrix)):
                if matrix[i]:
                    ans.append(matrix[i].pop(-1))
            if not matrix:
                continue
            add = matrix.pop(-1)
            add.reverse()
            ans = ans + add
            if not matrix:
                continue
            for i in range(len(matrix)-1, -1, -1):
                if matrix[i]:
                    ans.append(matrix[i].pop(0))
        return ans