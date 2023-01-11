import heapq
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        newCosts = []
        for index, cost in enumerate(costs):
            newCosts.append((cost, index))
        #print(newCosts)
        if candidates <= len(newCosts)//2:
            li = newCosts[:candidates] + newCosts[-candidates:]
            #newCosts = newCosts[candidates:-candidates]
            left = candidates
            right = len(costs) - candidates - 1
        else:
            li = newCosts
            left = 2
            right = 1
        #print(li)
       # print(newCosts)
        heapq.heapify(li)
        ans = 0
        for i in range(k):
            lowcost = heapq.heappop(li)
            #print("removing", lowcost)
            ans += lowcost[0]
            if left <= right:
                if lowcost[1] < left:
                    #print("adding", newCosts[0])
                    heapq.heappush(li, newCosts[left])
                    #newCosts = newCosts[1:]
                    left += 1
                else:
                    #print("adding", newCosts[-1])
                    heapq.heappush(li, newCosts[right])
                    #newCosts = newCosts[:-1]
                    right -= 1
        return ans
mySol = Solution()
print(mySol.totalCost([1,2,4,1], 3, 3))