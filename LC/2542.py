import heapq
class Solution:
    def maxScore(self, nums1, nums2, k: int) -> int:

        bottleneck = [(-nums2[i], nums1[i]) for i in range(len(nums1))]
        bottleneck.sort()

        bestscores = []
        #keep a heap of the best k - 1 scores where their nums2 won't interfere with us
        #

        for i in range(k-1):
            (num2, num1) = bottleneck.pop(0)
            heapq.heappush(bestscores, num1)
        
        ans = -1
        for num2, num1 in bottleneck:
            total = num1 + sum(bestscores)
            ans = max(ans, -num2 * total)
            heapq.heappushpop(bestscores, num1)
        return ans



       