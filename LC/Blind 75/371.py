class Solution(object):
    def getSum(self, a, b):
        mask = 0b11111111111111111111111111111111
        Max = 0b01111111111111111111111111111111
        if b == 0:
            return a if a <= Max else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )
mySol = Solution()
print(mySol.getSum(1,2))
print(mySol.getSum(2,3))
print(mySol.getSum(243,1235))