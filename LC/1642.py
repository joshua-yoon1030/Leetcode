import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        used_bricks = [0] * len(heights)
        for i in range(1, len(heights)):
            used_bricks[i] = max(0, heights[i] - heights[i-1])
        Lheap = []
        heapq.heapify(Lheap)

        for i in range(len(used_bricks)):
            heapq.heappush(Lheap, used_bricks[i])
            if len(Lheap) > ladders:
                bricks -= heapq.heappop(Lheap)
                if bricks < 0:
                    return i - 1
        return len(used_bricks)  -1


        
maxheap = [1,2,3]
heapq.heapify(maxheap)
print(heapq.heappop(maxheap))

        