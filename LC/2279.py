#2279, maxmimum bag with full capacity of rocks:
#strat: subtract and sort
#sorting: O(nlogn), all other opertaions are o(n)
class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        psum = [capacity[i] - rocks[i] for i in range(len(capacity))]
        psum.sort()
        total = 0
        for i in range(len(capacity)):
            if psum[i] > additionalRocks:
                return total
            else:
                additionalRocks -= psum[i]
                total += 1
        return total
        
        
mySol = Solution()
print(mySol.maximumBags([1,2,3], [4,5,6], 12))