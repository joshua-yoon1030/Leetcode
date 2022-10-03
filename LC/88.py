class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp1 = [i for i in nums1[:m]]
        i = 0 # temp 1
        j = 0 # nums 2 
        for x in range(len(nums1)):
            if i >= m:
                nums1[x] = nums2[j]
                j+= 1
            elif j >= n:
                nums1[x] = temp1[i]
                i+= 1
            elif temp1[i] < nums2[j]:
                nums1[x] = temp1[i]
                i+= 1
            else:
                nums1[x] = nums2[j]
                j+= 1

mySol = Solution()
print(mySol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))