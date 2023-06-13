from collections import defaultdict
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        counter = defaultdict(lambda: 0)
        for i in candidates:
            counter[i] += 1
        candidates = list(set(candidates))
        #print(candidates)
        def dp(j, stack):
            if sum(stack) > target:
                return
            if sum(stack) == target:
                #print("test")
                ans.append(list(stack))
                return
            if j >= len(candidates):
                return
            
            for i in range(counter[candidates[j]] + 1):
                dp(j + 1, list(stack))
                stack.append(candidates[j])

        dp(0, list())
        return ans

