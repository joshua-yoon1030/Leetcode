class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        #print(candidates)
        def dp(j, possible, target):
            #print(possible)
            if target == sum(possible):
                #print("made it")
                ans.append(list(possible))
                return
            if len(candidates) == j:
                return
            remaining = target - sum(possible)
            num = candidates[j]
            #print("remaining: ", remaining, "num: ", num, "test ", remaining // num)
            for i in range(remaining // num + 1):
               # print("test")
                dp(j + 1, list(possible), target)
                possible.append(num)

        dp(0, [], target)
        return ans
                
