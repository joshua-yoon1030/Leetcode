class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 2
        cur = nums[1]
        prev = nums[0]
        total = 0
        cd = cur - prev

        for i in range(2, len(nums)):
            cur = nums[i]
            prev = nums[i-1]
            if cd == cur - prev:
                count += 1
            else:
                cd = cur - prev
                count = 2
            total += max(count - 2, 0)
        return total