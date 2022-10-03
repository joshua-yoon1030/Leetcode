import collections
class Solution(object):
    def keyFn(self, z):
        x,y = z
        return y
    def mapFn(self, z):
        x, y = z
        return x
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        connections = collections.defaultdict(int)
        for i in range(n):
            connections[i] = 0
        for x,y in roads:
            connections[x] += 1
            connections[y] += 1
        connections = list(connections.items())
        connections = sorted(connections, key = self.keyFn)
        connections = list(map(self.mapFn, connections))
        #print(connections)
        importance = collections.defaultdict(int)
        count = 1
        for vertex in connections:
            importance[vertex] += count
            count += 1
        sum = 0
        #print(importance)
        for x,y in roads:
            sum += importance[x]
            sum += importance[y]
        return sum
mySol = Solution()
print(mySol.maximumImportance(5,[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(mySol.maximumImportance(5,[[0,3],[2,4],[1,3]]))
print(mySol.maximumImportance(5,[[0,1]]))