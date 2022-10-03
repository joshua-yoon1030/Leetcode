class Solution(object):
    def permute_help(self, nums):
        if len(nums) <= 1:
            return [nums]
        else:
            owo = []
            for i in range(len(nums)):
                #returns list of list, each list is one permutation
                left = nums[:i]
                right = nums[i+1:]
                #print(nums[i], left + right)
                permutes = self.permute_help(left + right)
                #permutes is list list, j is list
                for j in permutes:
                    j.append(nums[i])
                owo.extend(permutes)
            return owo

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = self.permute_help(nums)
        my_set = set(tuple(i) for i in permutations)
        return list(list(i) for i in my_set)