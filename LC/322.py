class Solution(object):
    coin_dict = dict()
    def coinChange1(self, coins, amount):
        if amount == 0:
            self.coin_dict[0] = 0
            return 0
        elif amount < 0: 
            return 9999999999999999
        elif amount in self.coin_dict:
            return self.coin_dict[amount]
        else:
            min = 9999999999999999
            for coin in coins:
                numCoin = self.coinChange1(coins, amount - coin)
                if numCoin < min:
                    min = numCoin
            self.coin_dict[amount] = min + 1
            return min + 1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = self.coinChange1(coins, amount)
        if ans > 9999999999999998:
            return -1
        else:
            return ans
        

#mySol = Solution()
#print(mySol.coinChange([2], 3))
