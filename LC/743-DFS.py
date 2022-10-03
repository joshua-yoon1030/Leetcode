class Solution(object):
    def DFS(self, adj_list, signal, curNode, curTime):
        #if our current time is slower than a node that we found, there's no need to dfs
        if(curTime > signal[curNode]):
            return
        signal[curNode] = curTime
        #run dfs again
        for neighbour, time in sorted(adj_list[curNode], key = lambda x: x[1]):
            self.DFS(adj_list, signal, neighbour, curTime + time)

    def sorting(self, x):
        (a,b) = x 
        return b

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #first we need to build an adj list
        adj_list = [[] for i in range(n + 1)]
        for time in times:
            u = time[0]
            v = time[1]
            w = time[2]
            adj_list[u].append((v,w))
            
        #then we make a signal list for our nodes 1 -> n
        #the default value should be something outrageously slow
        signal = [99999999999 for i in range(n+1)]

        curTime = 0
        #run DFS on our node k
        #DFS(adjlist, signalList, curNode, curTime)
        self.DFS(adj_list, signal, k, curTime)

        #find the longest node
        ans = max(signal[1:])
        if ans == 99999999999:
            return -1
        else:
            return ans

"""
mySol = Solution()
print(mySol.networkDelayTime([[1,2,1]], 2, 2))
"""


        