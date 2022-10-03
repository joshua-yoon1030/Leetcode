import collections
class Solution(object):
    #top down recursive approach
    #TLEs on last speed check even though its a valid solution
    #python sadge
    def dp(self, nums, target, ndict):
        if target == 0:
            return 1
        if ndict[target] > 0:
            return ndict[target]
        
        sum = 0
        for num in nums:
            if target >= num:
                sum += self.dp(nums, target - num, ndict)
        ndict[target] = sum
        return sum
        
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ndict = [-1] * (target + 1)
        ans = self.dp(nums, target, ndict)
        print(ndict)
        return ans
mySol = Solution()
print(mySol.combinationSum4([1,2,3], 4))
print(mySol.combinationSum4([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111], 999))
        