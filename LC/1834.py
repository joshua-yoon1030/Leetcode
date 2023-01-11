#1834: Single threaded CPU
#https://leetcode.com/problems/single-threaded-cpu/
#strategy: the tasks should be inserted into a min heap at their assigned time
#simulation might be too slow, might not be
import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        index = 0
        taskHeap = []
        heapq.heapify(taskHeap)
        time = 1
        ans = []
        
        while len(ans) != len(tasks):
            
            #adding to taskheap if the time has sufficiently passed
            while index < len(tasks) and tasks[index][0] <= time:
                #print("inserting", (tasks[index][1], index))
                heapq.heappush(taskHeap, (tasks[index][1], tasks[index][2]))
                index += 1
            if taskHeap:
                (procTime, ind) = heapq.heappop(taskHeap)
                #print("proccessing", (ind, procTime))
                time += procTime
                ans.append(ind)
            else:
                time = tasks[index][0]
        return ans