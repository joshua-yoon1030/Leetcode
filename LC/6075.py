class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        sublist = [0] * len(capacity)
        for i in range(len(capacity)):
            sublist[i]= capacity[i] - rocks[i]
        
        sublist.sort()

        counter = 0
        while additionalRocks >= 0:
            counter += 1
            if len(sublist) == 0:
                break
            additionalRocks -= sublist.pop(0)
        return counter - 1

mySol = Solution()
print(mySol.maximumBags([2,3,4,5],[1,2,4,4], 2 ))
print(mySol.maximumBags([10,2,2],[2,2,0], 100 ))
        