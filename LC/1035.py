from collections import defaultdict
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        bottom = defaultdict(list)
        for i in range(len(nums2)):
            bottom[nums2[i]].append(i) 
        
        def dp(i, maxB, bottom, memo):
            #Where i = the current index on the top you are checking
            #maxB = the farthest x coor on the bottom you have drawn a bridge to
            #bottom = dictionary matching number -> the xcoor on the bottom it is

            if i >= len(nums1):
                return 0 
            if (i, maxB) in memo:
                return memo[(i, maxB)]

            #two cases, we use a bridge or we don't
            ans = dp(i + 1, maxB, bottom, memo)
            for contender in bottom[nums1[i]]:
                if contender > maxB:
                    ans = max(ans, 1 + dp(i + 1, contender, bottom, memo))
            memo[(i, maxB)] = ans
            return ans
            


        
        memo = dict()
        return dp(0, -1, bottom, memo)

        
