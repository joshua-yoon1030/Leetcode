from collections import defaultdict
import heapq
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        head = headID
        for i in range(len(manager)):
            if manager[i] == -1:
                head = i
            else:
                graph[manager[i]].append(i)
        
        pqueue = [(0,head)]
        #format of pqueue is (time, employeeID)
        fastest = [0] * len(manager)
        
        while pqueue:
            (time, id) = heapq.heappop(pqueue)
            fastest[id] = time
            for neighbor in graph[id]:
                heapq.heappush(pqueue, (time + informTime[id], neighbor))
        return max(fastest)




