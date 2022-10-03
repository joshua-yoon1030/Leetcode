class Solution:
    def qs(self, nums, k):
        print(nums, k)
        partition = nums[0]
        less = list()
        greater = list()
        for i in range(1, len(nums)):
            if nums[i] < partition:
                less.append(nums[i])
            else:
                greater.append(nums[i])
        if len(less) == k:
            #our partition is the answer
            return partition
        elif len(less) < k:
            #right side
            return self.qs(greater, k - len(less) -1)
        else:
            #left side
            return self.qs(less, k)

    def findKthLargest(self, nums, k):
        # kinda like a binary search problem
        # We partition the whole set every time, and every time
        # the set gets 1/2 smaller on approximation
        # so this is an average O(N) problem
        # Notice how this method is noticably faster than the O(nlogn) sol
        # O(nlogn): just sort and index it lol ez gg
        k = len(nums) - k
        return self.qs(nums, k)
mySol = Solution()
print(mySol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))