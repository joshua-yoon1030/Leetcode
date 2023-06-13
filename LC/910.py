class Solution:
    def smallestRangeII(self, nums, k: int) -> int:
        nums.sort()
        score = nums[-1] - nums[0]
        maximum = nums[-1]
        minimum = nums[0]
        for i in range(len(nums) - 1):
            maximum = max(maximum, nums[i] + 2*k)
            minimum = min(nums[i] + 2 * k, nums[i+1])
            score = min(score, maximum - minimum)

        return score