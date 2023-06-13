class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, node):
            if node == self.parent[node]:
                return node
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
    def union(self, x,y):
        #print("merging", x, y)
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.size[py] += self.size[px]
            self.parent[px] = py

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        first = [-1] * (1 + max(nums))
        u = UF(len(nums))

        for i, x in enumerate(nums):
            for j in range(2, x):
                #fast prime factor finding
                if j * j > x:
                    break
                if x % j != 0:
                    continue
                #factor has been found: is it the first?
                if first[j] != -1: u.union(first[j], i)
                else:
                    first[j] = i
                while x % j == 0:
                    x //= j
            if x > 1:
                if first[x] != -1:
                    u.union(first[x], i)
                else:
                    first[x] = i
                    
        #print(parent)
        #print(size)
        return u.size[u.find(0)] == len(nums)