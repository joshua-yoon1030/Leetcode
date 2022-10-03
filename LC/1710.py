class Solution(object):
    def mapFn (self, a):
        return a[1]
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(reverse = True, key = self.mapFn)
        total = 0
        for numBox, units in boxTypes:
            #print("truckSize", truckSize)
            if numBox >= truckSize:
                #print("adding", truckSize)
                total += truckSize * units
                break
            else: # truckSize > numBox
                #print("adding", numBox)
                total += numBox * units
                truckSize -= numBox
        return total

mySol = Solution()
print(mySol.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))        
        