import collections
class Solution(object):
    #O(n^2) solution
    #strat: just iterate through the first number normally
    #then use a two pointer approach for the second and third numbers
    def threeSum(self, nums):

        nums.sort()
        ansList = []

        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                #checking the sum
                sum = nums[left] + nums[right] + nums[mid]
                #print("left", nums[left], "mid", nums[mid], "right", nums[right])
                if sum < 0:
                    mid += 1
                elif sum > 0:
                    right -= 1
                else:
                    ansList.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return ansList

mySol = Solution()
test1 = [-1,0,1,2,-1,-4]
test1.sort()
print(test1)
print(mySol.threeSum(test1))

#print(mySol.threeSum([0,0,0]))
#print(mySol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))