#134: Gas station
#https://leetcode.com/problems/gas-station/
#my strategy: You calculate the amount the gas changes at each stop
#if the sum of all the gas changing is negative you can't do it.
#then, the optimal part to start is right before the biggest drop in regards to the prefix sum
#idk i just stared at a couple examples and thought this would be right
#runtime: O(n) we only do single iterations
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        delta = [gas[i] - cost[i] for i in range(len(cost))]

        if sum(delta) < 0:
            return -1
        
        prefix = [0] * len(delta)
        prefix[0] = delta[0]
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] + delta[i]
        
        min = prefix[0]
        index = 0
        for i in range(1, len(prefix)):
            if prefix[i] < min:
                index = i
                min = prefix[i]
        return (index + 1) % len(prefix)
        