#39. Combination Sum
#https://leetcode.com/problems/combination-sum/
#Strategy: Just go through all the combinations I think
#edit: yeah thats basically it
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def findcombinations(candidates, target, stack):
            if target == 0:
                return [sorted(stack[::])]
            
            possible = []
            for candidate in candidates:
                if candidate <= target:
                    stack.append(candidate)
                    target -= candidate
                    possible += findcombinations(candidates, target, stack[::])
                    target+= candidate
                    stack.pop()
            return possible
        
        
        possible = findcombinations(candidates, target, [])
        possible.sort()
        i = len(possible)-1
        while i > 0:
            #print(i)
            if possible[i] == possible[i-1]:
                possible.pop(i)
            i -= 1
        
        return possible


            
        
        

mySol = Solution()
print(mySol.combinationSum([2,3,6,7], 7))
print(mySol.combinationSum([2,3,5], 8))
print(mySol.combinationSum([2], 1))       