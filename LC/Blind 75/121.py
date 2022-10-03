class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        smallest = prices[0]

        for p in prices:
            if smallest < p and (p - smallest) > diff:
                diff = p - smallest
            elif smallest > p:
                smallest = p
        return diff
