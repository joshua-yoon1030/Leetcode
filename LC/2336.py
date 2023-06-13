import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.infSet = set()
        for i in range(1, 1001):
            self.infSet.add(i)
        

    def popSmallest(self):
        """
        :rtype: int
        """
        ans = min(self.infSet)
        self.infSet.remove(ans)
        return ans
        
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.infSet.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)