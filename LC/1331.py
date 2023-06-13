import heapq
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rankQ = []

        for i in range(len(arr)):
            heapq.heappush(rankQ, (arr[i], i))
        
        rank = 0
        prev = 9999999999
        ans = [0] * len(arr)
        for i in range(len(arr)):
            (cur, index) = heapq.heappop(rankQ)
            if cur == prev:
                ans[index] = rank
                
            else:
                ans[index] = rank + 1
                rank += 1
            prev = cur
        return ans
        
