import collections
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        #the idea is that when we find what union a node is in,
        #we will traverse up the tree until we find the union.
        if x == self.root[x]:
            return x
        return self.find(self.root[x])
    
    def union(self, x, y):
        #first, find the representative nodes
        rootX = self.find(x)
        rootY = self.find(y)
        #if the two nodes are different, we have to union them
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution(object):
    def countPairs(self, n, edges):
        #run union find
        unions = UnionFind(n)
        for u, v in edges:
            unions.union(u,v)
        #get each group 
        group = [unions.find(i) for i in range(n)]
        counters = list(collections.Counter(group).values())
        sum = counters[0]
        ans = 0
        for i in range(1, len(counters)):
            ans += sum * counters[i]
            sum += counters[i]
        return ans
        

