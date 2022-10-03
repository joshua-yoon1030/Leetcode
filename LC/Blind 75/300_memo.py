import collections
class Solution(object):
    def dp(self, nums, maxi, index, ndict):
        #max: the current maximum in our subsequence
        #index: the index we are deciding to include/not include
        #count: the length of the subsequence
        #dict: entries are like (max, index)
        #Time O(n^2), space O(n^2) but it TLEs because python
        if index >= len(nums):
            return 0
        if ndict[(maxi,index)] > 0:
            return ndict[(maxi,index)]
        
        if nums[index] > maxi:
            include = 1 + self.dp(nums, nums[index], index + 1, ndict)
            dont = self.dp(nums, maxi, index + 1, ndict)
            ndict[(maxi, index)] = max(include, dont)
            return max(include, dont)
        else:
            dont = self.dp(nums, maxi, index + 1, ndict)
            ndict[(maxi, index)] = dont
            return dont

        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ndict = collections.defaultdict(lambda: -1)
        ans = self.dp(nums, -999999, 0, ndict)
        print(ndict)
        return ans
mySol = Solution()
#print(mySol.lengthOfLIS([10,9,2,5,3,7,101,18]))
#print(mySol.lengthOfLIS([0,1,0,3,2,3]))
#print(mySol.lengthOfLIS([7,7,7,7,7,7,7]))
#print(mySol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))