#835: Image Overlap
#https://leetcode.com/problems/image-overlap/
#My strategy: the img are 30x30 max, so just brute force.
class Solution(object):
    def shift_count(self, move, ref, up, right):
        #shifts the move picture up and right the specified number of steps
        #and then counts the overlapping region
        countright = 0
        countleft = 0
        for i in range(0, len(move) - up):
            for j in range(0, len(move) - right):
                if move[i+up][j] == ref[i][j + right] and ref[i][j + right] == 1:
                    countright += 1
                if ref[i][j] == move[i+up][j+right] and ref[i][j] == 1:
                    countleft += 1
        return max(countright, countleft)
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        maxcount = 0
        for i in range(len(img1)):
            for j in range(len(img1)):
                num1 = self.shift_count(img1, img2, i, j)
                num2 = self.shift_count(img2, img1, i, j)
                maxcount = max(num1, num2, maxcount)
        return maxcount
                

        