#1833: Maximum Ice cream bars
#https://leetcode.com/problems/maximum-ice-cream-bars/
#Strategy: Just sort and go through the list idk why this is a medium
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        i = 0
        while i < len(costs):
            if coins < costs[i]:
                break
            coins -= costs[i]
            i += 1
        return i
            


