from collections import defaultdict
import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        #graph building exercise
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row > 0:
                    graph[(row, col)].append((row-1, col, abs(heights[row][col] - heights[row - 1][col])))
                if row < len(heights) - 1:
                    graph[(row, col)].append((row+1, col, abs(heights[row][col] - heights[row + 1][col])))
                if col > 0:
                    graph[(row, col)].append((row, col-1, abs(heights[row][col] - heights[row][col - 1])))
                if col < len(heights[0]) - 1:
                    graph[(row, col)].append((row, col + 1, abs(heights[row][col] - heights[row][col + 1])))
        
        #pqueue in format: maximum absolute distance, row, col
        pqueue = [(0,0,0)]

        visited = set()
        while pqueue:
            (mad, row, col) = heapq.heapppop(pqueue)

            if (row, col) in visited:
                continue
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return mad

            visited.add((row, col))

            for (nr, nc, weight) in graph[(row, col)]:
                heapq.heappush(pqueue, (max(weight, mad), nr, nc))





