from collections import deque
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def buildnumber(stack1, stack2):
            ans = []
            while len(stack1) > 0 or len(stack2) > 0:
                if not stack1:
                    ans.append(stack2.pop())
                elif not stack2:
                    ans.append(stack1.pop())
                elif stack1[-1] > stack2[-1]:
                    ans.append(stack1.pop())
                else:
                    ans.append(stack2.pop())
            return ans
        
        stack1 = deque()
        stack2 = deque()
        
        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if 
