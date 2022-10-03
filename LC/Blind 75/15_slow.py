import collections
class Solution(object):
    #O(n^2 log n) solution, iterate through two indicies and binsearch last one
    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            #print("searching", low, high)
            mid = low + (high - low)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1 
        return False

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ansList = []
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                remaining = nums[j+1:]
                #print(i, j, remaining)
                target = -(nums[i] + nums[j])
                binS = self.binarySearch(remaining, target)
                if binS:
                    #print("added")
                    ansList.append( [nums[i], nums[j], target])
        #print(ansList)
        for i in ansList:
            i.sort()
        #print(ansList)
        ansList = set(tuple(i) for i in ansList)
        ansList = list(list(i) for i in ansList)
        return ansList

mySol = Solution()
#print(mySol.threeSum([-1,0,1,2,-1,-4]))

#print(mySol.threeSum([0,0,0]))
print(mySol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(mySol.binarySearch([-1,-4,-2,-3,3,0,4], -2))
            