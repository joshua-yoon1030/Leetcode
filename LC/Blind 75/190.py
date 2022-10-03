class Solution:
    # @param n, an integer
    # @return an integer
    def count(self, n, array):
            array.append(n & 1)
            return self.count(n >> 1, array)
    def reverseBits(self, n):
        mask = 0b11111111111111111111111111111111
        n &= mask
        ans = [0] * 32
        for i in range(32):
            ans[i] = n & 1
            n = n >> 1
        string = ""
        for i in ans:
            string += str(i)
        print(string)
        return int(string, 2)
mySol = Solution()
print(mySol.reverseBits(0b00000010100101000001111010011100))
