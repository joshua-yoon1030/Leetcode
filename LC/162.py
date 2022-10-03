class Solution(object):
    def binarySearch(self, low, mid, high, n, nums):
        if mid >= high:
            return mid
        if mid <= low:
            return mid
        #setup
        left = 0
        right = 0
        if mid == 0:
            left = -99999999999
        else:
            left = nums[mid-1]
        if mid == n-1:
            right = -99999999999
        else:
            right = nums[mid + 1]
        
        #binary search casing
        if(left < nums[mid] and right < nums[mid]):
            return mid
        elif(left < nums[mid] and nums[mid] < right):
            return self.binarySearch(mid, (mid + high)//2, high, n, nums)
        else:
            return self.binarySearch(low, (low + mid)//2, mid, n, nums)



    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return nums.index(max(nums[1], nums[0]))
        else:
            return self.binarySearch(0, len(nums)//2, len(nums), len(nums), nums)

mySol = Solution()
print(mySol.findPeakElement([1,2,3,1]))
print(mySol.findPeakElement([1,2,1,3,5,6,4]))
print(mySol.findPeakElement([1,2,3,4,5,6,7]))
print(mySol.findPeakElement([1]))   
print(mySol.findPeakElement([5,4,3,2,1])) 
print(mySol.findPeakElement([1,2]))