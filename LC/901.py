#901.Online Stock Span
#https://leetcode.com/problems/online-stock-span/
#The idea is, for each stock, publish the last person that "beat it", and how far away that is
#in the case your new stock is smaller than the one before it, then it's just O(1)
#However, if it's bigger, you can reference all the other stocks that your stock beat, and traverse back
#almost like a linked list
class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        if len(self.stocks) == 0:
            self.stocks.append([price, 1])
            return 1
        else:
            lastprice = self.stocks[-1][0]
            if lastprice > price:
                self.stocks.append([price, 1])
                return 1
            else:
                beats = 1
                index = len(self.stocks) - 1
                while lastprice <= price and index >= 0:
                    beats += self.stocks[index][1]
                    index -= self.stocks[index][1]

                    lastprice = self.stocks[index][0]
                self.stocks.append([price, beats])
                return beats


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)