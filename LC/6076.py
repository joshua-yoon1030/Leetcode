from fractions import Fraction
class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        #dumb edge case
        if (len(stockPrices) == 1): return 0

        #sort by xcoor
        stockPrices = sorted(stockPrices, key=lambda stock: stock[0])
        #get individual slopes, slopes[i] is the slope between stock [i] and [i+1]
        slopes = [0.0] * (len(stockPrices) - 1)

        for i in range(len(stockPrices) - 1):
            slopes[i] = Fraction(stockPrices[i+1][1] - stockPrices[i][1] , stockPrices[i+1][0] - stockPrices[i][0])

        counter = 1
        for i in range(len(slopes) - 1):
            if slopes[i] != slopes[i+1]:
                counter += 1
        return counter
        
mySol = Solution()
#print(mySol.minimumLines([[1,7],[2,7],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
#print(mySol.minimumLines([[3,4],[1,2],[7,8],[2,3]]))
print(mySol.minimumLines([[1,1], [2,1]]))
print(mySol.minimumLines([[93,6],[87,11],[26,58],[28,1],[69,87],[45,59],[29,3],[5,58],[60,94],[46,54],[38,58],[88,10],[94,7],[72,96],[2,93],[63,54],[74,22],[77,84],[33,64],[13,71],[78,59],[76,93],[3,31],[7,95],[68,32],[27,61],[96,31],[4,67],[75,36],[67,21],[8,66],[83,66],[71,58],[6,36],[34,7],[86,78]]))