class Solution(object):
    def binS(self,low, high,target, numbers):
        mid = low + (high - low) //2
        if low > high:
            #not found
            return -9999
        #print("searching ", numbers[mid])
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return self.binS(low, mid-1, target, numbers)
        else:
            return self.binS(mid+1, high, target, numbers)

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        Note: Has to only use constant space (no hashmap)
        """
        #step 1: iterate through all possible first numbers, and get the target we should find
        for i in range(len(numbers)):
            toFind = target - numbers[i]
            
            #step 2: binary search for second number
            #binS(low, high,target, numbers)
            #print("first num, ", numbers[i])
            index = self.binS(0, len(numbers)-1, toFind, numbers)
            if index != -9999 and i != index:
                
                return sorted([i+1, index+1])
mySol = Solution()
#print(mySol.twoSum([2,7,11,15], 9))
#print(mySol.twoSum([2,3,4], 6))
#print(mySol.twoSum([-1, 0], -1))