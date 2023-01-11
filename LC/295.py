#295: Find Median from data Stream
#https://leetcode.com/problems/find-median-from-data-stream/
#My Strategy: Two Heap approach
#If you have a max heap of elements less than the median, 
#and a min heap of elements greater than the median, you can update in log(n) time
#log(n) being you'd have to put an element in a heap after an update
#unfortunately, python only has heapq for minheaps, so to make a max heap we negate all values

import heapq
class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.median = 6969696969

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.median == 6969696969:
            self.median = num
            return
        
        if num < self.median:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -self.median)
            self.median = heapq.heappop(self.minheap)
        elif len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, self.median)
            self.median = -heapq.heappop(self.maxheap)


        

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.minheap) == len(self.maxheap):
            return self.median
        elif len(self.minheap) > len(self.maxheap):
            ans = (self.minheap[0] + self.median) /2.0
            return ans
        else:
            ans = (-self.maxheap[0] + self.median) /2.0
            return ans
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()