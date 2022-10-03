import collections
class Solution:
    def BFS(self,adj_list, signal, k, curTime):
        #put default k onto the queue
        queue = collections.deque([(curTime,k)])

        while queue:
            curTime, curNode = queue.popleft()
            #only traverse if we have a faster time
            if (curTime < signal[curNode]):
                signal[curNode] = curTime
                for neighbor, weight in adj_list[curNode]:
                    #add everything onto the queue
                    queue.append((curTime + weight, neighbor))

    def networkDelayTime(self, times, n, k):
        #first we need to build an adj list
        adj_list = collections.defaultdict(list)
        for time in times:
            u = time[0]
            v = time[1]
            w = time[2]
            adj_list[u].append((v,w))
            
        #then we make a signal list for our nodes 1 -> n
        #the default value should be something outrageously slow
        signal = [0] + [float("inf")] * n
        
        curTime = 0
        #run BFS on our node k
        self.BFS(adj_list, signal, k, curTime)

        #find the longest node
        ans = max(signal[1:])
        if ans < float("inf"):
            return ans
        else:
            return -1
#mySol = Solution()
#print(mySol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4,2))
