class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        boundary = nums[0]

        while left <= right:
            mid = left + (right - left)//2
            
            if(nums[mid] == target):
                return mid

            #cases to look right
            elif((target < boundary <= nums[mid]) or
                (nums[mid] <= target < boundary) or
                (boundary <= nums[mid] < target)):
                left = mid + 1
            else:
                right = mid - 1
        return -1
mySol = Solution()
print(mySol.search([4,5,6,7,0,1,2], 0))
print(mySol.search([4,5,6,7,0,1,2], 3))
print(mySol.search([1,3], 3))
        
        