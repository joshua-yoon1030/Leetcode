class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        Note: Has to only use constant space (no hashmap)
        """
        low = 0
        high = len(numbers)-1
        while low <= high:
            check = numbers[low] + numbers[high]
            if check == target:
                return [low + 1, high + 1]
            elif(check < target):
                low +=1
            else:
                high -= 1
mySol = Solution()
print(mySol.twoSum([2,7,11,15], 9))
print(mySol.twoSum([2,3,4], 6))
print(mySol.twoSum([-1, 0], -1))