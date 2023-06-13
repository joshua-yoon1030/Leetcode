import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        pqueue = []
        workers = sorted(lambda q, w: (q/(w + 0.0)) for q, w in zip(quality, wage))
        for work in workers:
            print(work)

