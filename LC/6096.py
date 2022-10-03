class Solution(object):
    def binS(self,low, high,target, numbers, spell):
        mid = low + (high - low) //2
        if low > high:
            #not found
            return (low, high)
        elif numbers[mid] * spell >= target:
            return self.binS(low, mid-1, target, numbers, spell)
        else:
            return self.binS(mid+1, high, target, numbers, spell)
        

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        ans = [0] * len(spells)
        for i in range(len(spells)):
            (cand1, cand2) = self.binS(0, len(potions)-1, success, potions, spells[i])
            ans[i] = len(potions) - max(cand1, cand2)
        return ans
mySol = Solution()
print(mySol.successfulPairs([5,1,3], [1,2,3,4,5],7))
print(mySol.successfulPairs([3,1,2],[8,5,8], 16))