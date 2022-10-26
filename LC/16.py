#16: 3Sum Closest
#https://leetcode.com/problems/3sum-closest/
#My strategy: First sort the array
#then have a two pointer approach. Select the first number, and two pointer the last two numbers
#Runtime: O(n^2): O(n) outside loop and O(n) work in each loop
#sorting is O(nlogn)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target-sum)<abs(target-min) :
                    min = sum
                if sum < target:
                    #too small, we need bigger numbers
                    left += 1
                elif sum > target:
                    #too large, we need smaller numbers
                    right -= 1
                else:
                    #sum == target
                    return target
        return min

        